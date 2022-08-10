# Import everything needed to edit video clips
from moviepy.editor import *

# loading video gfg
source = input("Source: ")
clip = VideoFileClip(source)

# getting only first 5 seconds
start_seconds = int(input("Start seconds: "))
start_minutes = int(input("Start minutes: "))
start_hours = int(input("Start hours: "))
end_seconds = int(input("End seconds: "))
end_minutes = int(input("End minutes: "))
end_hours = int(input("End hours: "))

try:
    clip = clip.subclip(
        (start_hours * 3600 + start_minutes * 60 + start_seconds),
        (end_hours * 3600 + end_minutes * 60 + end_seconds)
    )
except IOError:
    print("problem cropping file..")

# showing clip
clip.write_videofile(source.replace('.mkv', '_cropped.mp4'), fps=25)
