import os
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from pytube import YouTube
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.config import Config

# demo video URL:
# https://youtu.be/2FydDzKecpI

from multiprocessing import Process, Queue, Event
from threading import Thread

queue = Queue()

Config.set('graphics', 'fullscreen', 'auto')
Config.set('graphics', 'window_state', 'maximized')
Config.write()

# YouTubeGUI class
class YouTubeScreen(BoxLayout):

    def __init__(self, **kwargs):
        super(YouTubeScreen, self).__init__(**kwargs)

        self.orientation = 'vertical'

        self.requestLayout = BoxLayout(
            orientation='vertical'
        )

        self.downloadsLayout = BoxLayout(
            orientation='vertical'
        )

        self.url_label = Label(
            text='Video URL',
            size_hint_y=None,
            height=20
        )

        self.url_field = TextInput(
            multiline=False,
            size_hint=(1, None),
            height=40,
        )

        self.name_label = Label(
            text='Name of Video',
            size_hint_y=None,
            height=20
        )

        self.name_field = TextInput(
            multiline=False,
            size_hint=(1, None),
            height=40,
        )

        self.downloadButton = Button(
            text='Download',
            size_hint=(1, None),
            height=40,
            pos_hint={'center_x': .5, 'center_y': .5}
        )
        self.downloadButton.bind(on_press=self.onClick)

        self.requestLayout.add_widget(self.url_label)
        self.requestLayout.add_widget(self.url_field)
        self.requestLayout.add_widget(self.name_label)
        self.requestLayout.add_widget(self.name_field)

        self.add_widget(self.downloadsLayout)
        self.add_widget(self.requestLayout)
        self.add_widget(self.downloadButton)

    # function to be called when download button is clicked
    def onClick(self, instance):
        thread = Thread(target=self.startDownload, daemon=True).start()
        self.pb = ProgressBar(
            max=100, 
            value=0,
            size_hint=(1, None),
            height=20,
            pos_hint={'center_x': .5, 'center_y': .5}
        )
        self.downloadsLayout.add_widget(self.pb)

    # function to be called when download is in progress
    def onProgress(self, stream, chunk, bytes_remaining):
        """ Updates progress bar with current download progress. """
        print(f'\nDownloading: {self.yt.title}')
        percentage = 100 * (1 - bytes_remaining / stream.filesize)
        self.pb.value = int(percentage)
        print(f'\nDownload progress: {percentage}%')
        if bytes_remaining == 0:
            print('\nDownload complete!')
            self.pb.value = 0

    # function to be called to start downloading
    def startDownload(self):
        """ Instantiates YouTube class and downloads selected video.  
        Built-in pytube.cli function on_progress can alternatively be used 
        to show a DOS style progress bar. """

        # YouTube video object
        self.yt = YouTube(
            self.url_field.text,
            on_progress_callback=self.onProgress
        )
        
        # creates download and downloads to subdirectory called 'downloads'
        video_file = self.yt.streams.get_highest_resolution().download(
            output_path=os.getcwd() + '\\.downloads\\',
            filename=self.name_field.text + '.mp4',
        )

        queue.put_nowait(video_file)


# class to create the application
class MyApp(App):

    def build(self):
        return YouTubeScreen()


# run the application
if __name__ == '__main__':
    MyApp().run()
