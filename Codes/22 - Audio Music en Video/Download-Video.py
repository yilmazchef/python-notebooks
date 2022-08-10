import os
from pytube import YouTube
from pytube.cli import on_progress
import cv2

fuchsia = '\033[38;2;255;00;255m'  # color as hex #FF00FF
reset_color = '\033[39m'

# url is url of youtube video to download.


def download_youtube(url):
    """ Instantiates YouTube class and downloads selected video.  Uses Built-in
    pytube.cli function on_progress to show a DOS style progress bar. """
    yt = YouTube(url, on_progress_callback=on_progress)

    # following line displays title and number of times video has been viewed.
    print(f'\n' + fuchsia + 'Downloading: ',
          yt.title, '~ viewed', yt.views, 'times.')

    # creates download and downloads to subdirectory called 'downloads'
    yt.streams.get_highest_resolution().download('.\\.downloads\\')

    # displays message verifying download is complete, and resets color scheme
    # back to original color scheme.
    print(f'\nFinished downloading:  {yt.title}' + reset_color)


def play_video(path):

    # Create a VideoCapture object and read from input file
    cap = cv2.VideoCapture(path)

    # Check if camera opened successfully
    if (cap.isOpened() == False):
        print("Error opening video file")

    # Read until video is completed
    while(cap.isOpened()):

        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:

            # Display the resulting frame
            cv2.imshow('Frame', frame)

            # Press Q on keyboard to exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Break the loop
        else:
            break

    # When everything done, release
    # the video capture object
    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()


if __name__ == '__main__':

    # downloads video from youtube url
    download_youtube(input('Enter YouTube URL: '))
    # plays video from local directory
    play_video('.\\.downloads\\' + input('Enter video name: '))
