'''
This file is used to run various versions of the YOLO object detection model for real-time inference over a live webcam or previously recorded video
'''

from ultralytics import YOLO

# To run the YOLO object detection model on live webcam:
model = YOLO('yolo11s.pt') # standard pretrained YOLOv11s object detection model
#model = YOLO('pen_detect.pt') # model we fine-tuned on pen dataset
results = model(source=0, show=True, conf=0.3, save=True)

# To run the YOLO object detection model on previously recorded video:
#model = YOLO('yolo11s.pt')
#model(source='bond.mp4', show=True, conf=0.3, vid_stride=3)

'''
# Previously, you could run inference directly on a youtube link, but this sadly no longer works (youtube detects as a bot)
# Now we have to download the video first using youtube-dl or similar tool (see download_videos.py)

# Clip from Casino Royale::
results = model(source="https://www.youtube.com/watch?v=iZxNbAwY_rk", show=True)
'''