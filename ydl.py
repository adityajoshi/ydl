from pytube import YouTube
import argparse
import sys

try:
    parser = argparse.ArgumentParser(description="ydl is a command line tool \
    to download YouTube video.")
    parser.add_argument('url',type=str, help='Input URL to video')

    args = parser.parse_args()
    print("Working for url " + args.url)
    yt = YouTube(args.url)
    print("Video url is configured.")
    video_path = yt.streams.first().download()
    print("Video is downloaded.")
except Exception as e:
    # e = sys.exc_info()[0]
    print(e)
