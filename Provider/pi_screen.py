import time
from PIL import Image

class screen():
    def __init__(self):
        self.PATH = "screenshot/"
        self.DEFAULT_NAME = "screenshot/clone.jpg"
        self.ERROR_STATUS = "ERROR: screen.copy_image() func"

    def copy_image(self):
        now = time.localtime()
        filename = "Screenshot_%04d-%02d-%02d_%02d-%02d-%02d.jpg" % (
            now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

        path = self.PATH + filename
        im = Image.open(self.DEFAULT_NAME)
        im.save(path)

        return filename

    def send_image(self):
        try:
            filename = self.copy_image()
        except:
            filename = self.ERROR_STATUS
            print(filename)

        return filename

# test code
# sc = screen()
# sc.capture()
