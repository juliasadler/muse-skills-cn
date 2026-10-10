#!/usr/bin/env python3
"""视频转逐字稿：转写 + 说话人分离 + 话轮合并。

输出样式示例：
    [00:00:00] 说话人A：同一人连续说的完整的话……

用法：
    python diarize_transcribe.py 音频.wav --speakers 2 --out 逐字稿.txt
"""
import argparse
import numpy as np
import soundfile as sf
import torch
from faster_whisper import WhisperModel
from speechbrain.inference import EncoderClassifier
from sklearn.cluster import AgglomerativeClustering


def fmt_ts(sec: float) -> str:
    h = int(sec // 3600)
    m = int(sec % 3600 // 60)
    s = int(sec % 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("audio", help="输入音频（16kHz 单声道 wav 最佳）")
    ap.add_argument("--speakers", type=int, default=2, help="说话人数")
    ap.add_argument("--model", default="small", help="whisper 模型尺寸")
    ap.add_argument("--language", default="zh", help="转写语言")
    ap.add_argument("--out", default="transcript.txt", help="输出文件")
    ap.add_argument("--names", default="", help="说话人名字，逗号分隔，如 '邵艾伦,孙宇晨'（顺序对应聚类标签0,1…，不填则用说话人A/B）")
    args = ap.parse_args()

    # 1. 转写
    print("转写中…")
    wm = WhisperModel(args.model, device="cpu", compute_type="int8")
    segments, info = wm.transcribe(args.audio, language=args.language, beam_size=5)
    segs = [(s.start, s.end, s.text.strip()) for s in segments if s.text.strip()]
    print(f"共 {len(segs)} 个片段，识别语言: {info.language}")

    # 2. 每个片段提说话人 embedding
    print("提取声纹中…")
    audio, sr = sf.read(args.audio)
    if audio.ndim > 1:
        audio = audio.mean(axis=1)
    classifier = EncoderClassifier.from_hparams(
        source="speechbrain/spkrec-ecapa-voxceleb",
        run_opts={"device": "cpu"},
    )
    embs = []
    for st, en, _ in segs:
        chunk = audio[int(st * sr):int(en * sr)].astype(np.float32)
        if len(chunk) < int(sr * 0.5):  # 太短的片段补齐，避免 embedding 不稳定
            chunk = np.pad(chunk, (0, int(sr * 0.5) - len(chunk)))
        with torch.no_grad():
            emb = classifier.encode_batch(torch.tensor(chunk).unsqueeze(0))
        embs.append(emb.squeeze().numpy())
    embs = np.stack(embs)

    # 3. 聚类分说话人
    labels = AgglomerativeClustering(
        n_clusters=args.speakers, metric="cosine", linkage="average"
    ).fit_predict(embs)

    # 4. 合并连续同一说话人的片段为话轮
    names = [n.strip() for n in args.names.split(",")] if args.names else []
    def spk_name(lab: int) -> str:
        if lab < len(names) and names[lab]:
            return names[lab]
        return f"说话人{chr(ord('A') + lab)}"

    turns = []
    for (st, en, text), lab in zip(segs, labels):
        if turns and turns[-1]["label"] == int(lab):
            turns[-1]["text"] += text
            turns[-1]["end"] = en
        else:
            turns.append({"label": int(lab), "start": st, "end": en, "text": text})

    # 5. 输出
    lines = [f"[{fmt_ts(t['start'])}] {spk_name(t['label'])}：{t['text']}" for t in turns]
    with open(args.out, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"共 {len(turns)} 个话轮，已写入 {args.out}")
    print()
    print("\n".join(lines))


if __name__ == "__main__":
    main()
