import os
from moviepy.editor import VideoFileClip, concatenate_videoclips
from prettytable import PrettyTable
import cv2
import datetime

def get_video_info(video_file) -> dict:
    # create video capture object
    data = cv2.VideoCapture(video_file)

    # count the number of frames
    frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = int(data.get(cv2.CAP_PROP_FPS))
    width = int(data.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(data.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # calculate duration of the video
    seconds = int(frames / fps)
    duration = str(datetime.timedelta(seconds=seconds))

    data = [
        {
            "source": video_file,
            "width": width,
            "height": height,
            "fps": fps,
            "frames": frames,
            "duration": duration,
            "seconds": seconds
        }
    ]

    return data

folder = input("Folder to merge videos: ")

video_files = [(folder + "/" + file) for file in os.listdir(folder) if (file.endswith(".mp4") or file.endswith(".mkv") or file.endswith(".mov"))]

video_clips = [VideoFileClip(file) for file in video_files]

x = PrettyTable()
x.field_names = ["Source", "Width", "Height", "FPS", "Frames", "Duration", "Seconds"]

for video_file in video_files:
    data = get_video_info(video_file)
    x.add_row(
        data[0].values()
    )

print(x)

if(len(video_files) > 0):
    final_video= concatenate_videoclips(video_clips)
    final_video.write_videofile("merged.mp4")
    
