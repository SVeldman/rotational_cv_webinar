#This code can be used to download various videos from youtube to run inference on with your YOLO pose estimation models
# These particular videos are a brief clip of a human walking and another of several tigers interracting with each other

# Requires previous installation of yt-dlp:
#!pip install yt-dlp

# Download video using yt-dlp:
import subprocess

video_url = "https://www.youtube.com/watch?v=Mol0lrRBy3g"
subprocess.run(['yt-dlp', '-o', 'walking_video.mp4', video_url])

video_url = "https://www.youtube.com/watch?v=JMsCJhGtPKM"
subprocess.run(['yt-dlp', '-o', 'tiger_video.mp4', video_url])

video_url = "https://www.youtube.com/watch?v=iZxNbAwY_rk"
subprocess.run(['yt-dlp', '-o', 'bond.mp4', video_url])