# -*- coding:utf-8 -*-

import argparse
import json
import os
import wave


def make_data_json(src, dst):
    """
    파일을 분석해서 json 형태로 저장
    :param src: src data directory
    :param dst: save json filename
    """
    with open(dst, "w") as o_f:
        for group in os.listdir(src):
            group_path = os.path.join(src, group)
            for speaker in os.listdir(group_path):
                labels_file = os.path.join(group_path, speaker, f"{group}-{speaker}.trans.txt")
                with open(labels_file) as i_f:
                    for line in i_f:
                        split = line.strip().split()
                        file_id = split[0]
                        label = " ".join(split[1:]).lower()
                        wavfile = os.path.join(group_path, speaker, f"{file_id}.wav")
                        assert os.path.exists(wavfile)

                        # duration 계산
                        audio = wave.open(wavfile)
                        duration = float(audio.getnframes()) / audio.getframerate()
                        audio.close()

                        data = {"key": wavfile, "duration": duration, "label": label}
                        o_f.write(json.dumps(data))
                        o_f.write("\n")


def main(args):
    """
    main function
    :param args: input arguments
    """
    for dir in os.listdir(args.wav_dir):
        data_dir = os.path.join(args.wav_dir, dir)
        if os.path.isdir(data_dir):
            make_data_json(data_dir, os.path.join(args.wav_dir, f"{dir}.json"))


def parse_args():
    """
    build arguments
    :return args: input arguments
    """
    parser = argparse.ArgumentParser(description="Flack to wave arguments.")
    parser.add_argument("--wav_dir", type=str, default="../../data/LibriSpeech/wav", required=False, help="LibriSpeech wav directory")

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    main(args)