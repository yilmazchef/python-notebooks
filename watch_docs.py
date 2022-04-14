# import time module, Observer, FileSystemEventHandler
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from update_docs import list_files, to_md, to_docx


class OnMyWatch:
    # Set the directory on watch
    watchDirectory = os.getcwd()

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(
            event_handler, self.watchDirectory, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            ipynb_file_list = list_files(event.src_path, ".ipynb")

            for ipynb_file in ipynb_file_list:
                md_file = ipynb_file.replace(".ipynb", ".md")
                docx_file = ipynb_file.replace(".ipynb", ".docx")

                print("#" * 255)

                to_md(ipynb_file, md_file)
                to_docx(md_file, docx_file)

                print("#" * 255)

            print("#" * 255)
            print("#" * 80, end="")
            print("THE CONVERSION IS COMPLETED..", end="")
            print("#" * 80, end="\n")
            # Event is created, you can process it now
            print("Watchdog received created event - % s." % event.src_path)
        elif event.event_type == 'modified':
            # Event is modified, you can process it now
            print("Watchdog received modified event - % s." % event.src_path)


if __name__ == '__main__':
    watch = OnMyWatch()
    watch.run()
