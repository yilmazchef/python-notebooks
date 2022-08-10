import os
from pytube import YouTube
from pytube.cli import on_progress
import vlc

fuchsia = '\033[38;2;255;00;255m'  # color as hex #FF00FF
reset_color = '\033[39m'

def download_youtube(url):
    """ Instantiates YouTube class and downloads selected video.  Uses Built-in
    pytube.cli function on_progress to show a DOS style progress bar. """
    yt = YouTube(url, on_progress_callback=on_progress)

    # following line displays title and number of times video has been viewed.
    print(f'\n' + fuchsia + 'Downloading: ',
          yt.title, '~ viewed', yt.views, 'times.')

    # creates download and downloads to subdirectory called 'downloads'
    video = yt.streams.filter(only_audio=True).first()
    audio = video.download('.\\.downloads\\')

    # save the file
    base, ext = os.path.splitext(audio)
    new_file = base + '.mp3'
    os.rename(audio, new_file)

    # displays message verifying download is complete, and resets color scheme
    # back to original color scheme.
    print(f'\nFinished downloading:  {yt.title}' + reset_color)

    return new_file


def play_music(path):
    """PyAudio Example: Play a wave file."""

    p = vlc.MediaPlayer(path)
    p.play()
    


if __name__ == '__main__':

    # downloads video from youtube url
    inAudio = input('Enter youtube url: ')

    outAudio = download_youtube(inAudio)
    # plays music from local directory
    play_music(outAudio)

