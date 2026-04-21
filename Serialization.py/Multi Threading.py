from threading import Thread
import time
class VLC(Thread):
    def run(self):
        print("VLC apl opened")
        time.sleep(3)
class Video_start(Thread):
    def run(self):
        print("Video started playing")
        time.sleep(3)
class audio_start(Thread):
    def run(self):
        print("Audio started playing")
        time.sleep(3)
class prog_bar(Thread):
    def run(self):
        print("Progress Bar is activated")
        time.sleep(3)
class volume(Thread):
    def run(self):
        print("Volume is increasing")
        time.sleep(3)
v1=VLC()
v2=Video_start()
v3=audio_start()
v4=prog_bar()
v5=volume()
v1.start()
v2.start()
v3.start()
v4.start()
v5.start()
print("VLC application closed")
