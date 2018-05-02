import time
from PIL import Image
from requests_toolbelt import MultipartEncoder
import requests


class screen():
    def __init__(self):
        self.PATH = "screenshot/"
        self.DEFAULT_NAME = "screenshot/clone.jpg"
        self.ERROR_STATUS = "ERROR: screen.copy_image() func"
        self.URL = "http://localhost:8000/uploaded"

    def copy_image(self):
        now = time.localtime()
        filename = "Screenshot_%04d-%02d-%02d_%02d-%02d-%02d.jpg" % (
            now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

        path = self.PATH + filename
        im = Image.open(self.DEFAULT_NAME)
        im.save(path)

        return filename

    def send_image_to_server(self, filename):
        print("Post Server :" + self.URL + ", filname :" + filename)
        f = open(self.PATH + filename, 'rb')
        m = MultipartEncoder({'image': (f.name, f, 'text/plain')})
        try:
            requests.post(self.URL, data=m, headers={'Content-Type': m.content_type})
        except:
            print("Post is Failed, maybe Server is Down or URL is incorrect.")

# test code
# sc = screen()
# sc.capture()
