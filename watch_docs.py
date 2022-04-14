import os
import sys
import time
import watchdog.events
import watchdog.observers
from update_docs import to_md, to_docx


class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        # Set the patterns for PatternMatchingEventHandler
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.ipynb'],
                                                             ignore_directories=True, case_sensitive=False)

    def on_created(self, event):
        print("Watchdog received created event - % s." % event.src_path)
        # Event is created, you can process it now

    def on_modified(self, event):
        print("Watchdog received modified event - % s." % event.src_path)
        # Event is modified, you can process it now
        md_file = event.src_path.replace(".ipynb", ".md")
        docx_file = event.src_path.replace(".ipynb", ".docx")
        print("#" * 255)
        to_md(event.src_path, md_file)
        to_docx(md_file, docx_file)
        print("#" * 255)
        print("#" * 255)
        print("#" * 80, end="")
        print("THE CONVERSION IS COMPLETED..", end="")
        print("#" * 80, end="\n")

    def on_deleted(self, event):
        print("Watchdog received delete event - % s." % event.src_path)
        md_file = event.src_path.replace(".ipynb", ".md")
        docx_file = event.src_path.replace(".ipynb", ".docx")
        print("#" * 255)
        os.remove(md_file)
        os.remove(docx_file)
        print("#" * 255)
        print("#" * 255)
        print("#" * 80, end="")
        print("THE NOTEBOOK, ITS RELATED MARKDOWN FILE AND WORD DOCUMENT ARE DELETED..", end="")
        print("#" * 80, end="\n")


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
