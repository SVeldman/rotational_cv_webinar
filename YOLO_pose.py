'''
This file is used to run various versions of the YOLO pose estimation model for real-time inference using either a live webcam or previously recorded video
'''

from ultralytics import YOLO

model = YOLO('yolo11n-pose.pt') # standard pretrained YOLOv11n pose estimation model
hand_model = YOLO('hand_model.pt') # model we fine-tuned on hand keypoint dataset
tiger_model = YOLO('tiger_model.pt') # model we fine-tuned on tiger keypoint dataset

#To run the YOLO pose estimation model on a live webcam feed:
results = model(source=0, show=True, conf=0.3, save=True)

#To run the fine-tuned hand keypoint model on a live webcam feed:
#results = hand_model(source=0, show=True, conf=0.3, save=True)

# To run the standard YOLO pose estimation model on a previously recorded video:
#model(source="walking_video.mp4", show=True)

# To run the fine-tuned tiger pose estimation model on a previously recorded video:
#tiger_model(source="tiger_video.mp4", show=True)



'''
# Previously, you could run inference directly on a youtube link, but this sadly no longer works (youtube detects as a bot)
# Now we have to download the video first using youtube-dl or similar tool (see download_videos.py)

# Video of human walking:
while True:
    results = model(source="https://www.youtube.com/watch?v=Mol0lrRBy3g", show=True)'

# Video of tigers:
results = tiger_model(source="https://www.youtube.com/watch?v=JMsCJhGtPKM", show=True)
'''