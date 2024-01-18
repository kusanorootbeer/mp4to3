from moviepy.editor import VideoFileClip
import os
import sys

def convert_to_mp3(mp4_file, mp3_file):
    video = VideoFileClip(mp4_file)
    audio = video.audio
    audio.write_audiofile(mp3_file)
    audio.close()
    video.close()

# コマンドライン引数からmp4ファイルのパスを取得
mp4_file = sys.argv[1]

# mp4ファイルの拡張子を.mp3に変更してmp3ファイルのパスを作成
mp3_file = os.path.splitext(mp4_file)[0] + ".mp3"

# 変換を実行
convert_to_mp3(mp4_file, mp3_file)