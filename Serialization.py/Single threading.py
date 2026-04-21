import time
class VLC:
    def apl_open(self):
        print("VLC apl opened")
        time.sleep(3)
    def video_start(self):
        print("Video started playing")
        time.sleep(3)
    def audio_start(self):
        print("Audio started playing")
        time.sleep(3)
    def prog_bar(self):
        print("Progress Bar is activated")
        time.sleep(3)
    def volume(self):
        print("Volume is increasing")
        time.sleep(3)
v=VLC()
v.apl_open()
v.video_start()
v.audio_start()
v.prog_bar()
v.volume()
print("VLC application closed")