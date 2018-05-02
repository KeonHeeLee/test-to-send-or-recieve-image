import time, requests

class util:
    def __init__(self):
        self.PATH = "upload/"
        self.HOST = "http://localhost:9000/image"
        self.HEADER = {"Content-Type": "application/json;charset=UTF-8"}
        self.SUCCESS = "이미지 수신에 성공하였습니다."
        self.FAIL = "이미지 수신에 실패하였습니다."

    def request_image(self):
        response = requests.post(url=self.HOST, param=self.HEADER)
        return response

    def reply_analyzer(self):
        now = time.localtime()
        response = self.request_image()

        if response.status_code == 500:
            return False
        else:
            return True

    def recieving_image_status(self, user):
        if self.reply_analyzer() : sendMSG = self.SUCCESS
        else : sendMSG = self.FAIL

        message = {
            "event": "send",
            "user" : user,
            "textContent": {
                "text": sendMSG
            }
        }
        return message
