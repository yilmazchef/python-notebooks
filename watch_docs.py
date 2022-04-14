import os
import sys
import time
import watchdog.events
import watchdog.observers
from update_docs import to_md, to_docx, to_odt, to_py


class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        # Set the patterns for PatternMatchingEventHandler
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.ipynb'],
                                                             ignore_directories=True, case_sensitive=False)

    def on_created(self, event):
        print("#" * 255)
        print(f"{event.src_path} is created.")
        # Event is created, you can process it now
        print("#" * 255)

    def on_modified(self, event):
        print("#" * 255)
        print(f"{event.src_path} is modified.")
        # Event is modified, you can process it now
        md_file = event.src_path.replace(".ipynb", ".md")
        docx_file = event.src_path.replace(".ipynb", ".docx")
        to_md(event.src_path, md_file)
        print(f"{md_file} is modified.")
        to_docx(md_file, docx_file)
        print(f"{docx_file} is modified.")
        print("#" * 255)

    def on_deleted(self, event):
        print("#" * 255)
        print(f"{event.src_path} is deleted.")
        md_file = event.src_path.replace(".ipynb", ".md")
        docx_file = event.src_path.replace(".ipynb", ".docx")
        os.remove(md_file)
        print(f"{md_file} is deleted.")
        os.remove(docx_file)
        print(f"{docx_file} is deleted.")
        print("#" * 255)


if __name__ == "__main__":
    src_path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    event_handler = Handler()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
