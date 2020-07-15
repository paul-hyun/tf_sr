# -*- coding:utf-8 -*-

import argparse
import os
import shutil
import sys
from pydub import AudioSegment


def flac_to_wav(src, dst):
    """
    flac을 wav로 변경 (나머지는 복사)
    :param src: flac directory
    :param dst: wav directory
    """
    for filename in os.listdir(src):
        src_path = os.path.join(src, filename)
        dst_path = os.path.join(dst, filename)

        if os.path.isdir(src_path):
            # 존재 하지 않으면 파일 생성
            if not os.path.isdir(dst_path):
                os.makedirs(dst_path)
            flac_to_wav(src_path, dst_path)
        elif os.path.isfile(src_path):
            # falc to wav
            if src_path.endswith(".flac"):
                filename, _ = os.path.splitext(dst_path)
                # 파일이 존재하지 않을 경우 wav 생성
                if not os.path.exists(f"{filename}.wav"):
                    src_flac = AudioSegment.from_file(src_path, format="flac")
                    src_flac.export(f"{filename}.wav", format="wav")
            else:
                # 파일이 존재하지 않을 경우 복사
                if not os.path.exists(dst_path):
                    shutil.copy(src_path, dst_path)
        else:
            raise ValueError(src_path)


def main(args):
    """
    main function
    :param args: input arguments
    """
    flac_to_wav(args.flac_dir, args.wav_dir)


def parse_args():
    """
    build arguments
    :return args: input arguments
    """
    parser = argparse.ArgumentParser(description="Flac to wave arguments.")
    parser.add_argument("--flac_dir", type=str, default="../../data/LibriSpeech/flac", required=False, help="LibriSpeech flac directory")
    parser.add_argument("--wav_dir", type=str, default="../../data/LibriSpeech/wav", required=False, help="LibriSpeech wav directory")

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    main(args)
