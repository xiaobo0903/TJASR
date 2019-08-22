# -*- coding: utf-8 -*-
'''因为听鉴针对的是开放空间的语音识别,所以需要在静音训练文件中增加噪音
'''

import argparse
import json
import os

import librosa
import numpy as np


def add_noise(audio_path, out_path, percent=0.045, sr=16000):

    src, sr = librosa.load(audio_path, sr=sr)
    random_values = np.random.rand(len(src))
    src = src + percent * random_values
    librosa.output.write_wav(out_path, src, sr, norm=True)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--audio_dir", type=str)
    parser.add_argument("--out_dir", type=str)

    args = parser.parse_args()

    if not os.path.exists(args.out_dir):
        os.makedirs(args.out_dir)

    for root, dirs, files in os.walk(args.audio_dir):

        for file in files:

            if not file.endswith(".wav"):
                continue

            audio_path = os.path.join(root, file)
            out_path = os.path.join(args.out_dir, file)
            add_noise(audio_path, out_path)
