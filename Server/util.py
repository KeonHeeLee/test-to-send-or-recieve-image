import time, requests

class util:
    def __init__(self):
        self.PATH = "uploaded/"
        self.HOST = "http://localhost:9000/image"
        self.HEADER = {"Content-Type": "application/json;charset=UTF-8"}
        self.SUCCESS = "이미지 수신에 성공하였습니다."
        self.FAIL = "이미지 수신에 실패하였습니다."

    def request_image(self):
        response = requests.post(url=self.HOST, headers=self.HEADER)
        return response

    def reply_analyzer(self):
        now = time.localtime()
        response = self.request_image()
        if response.status_code == 500:
            return False
        else:
            data = response.json()
            filename = data["path"]
            return True, filename

    def recieving_image_status(self, user):
        result, filename = self.reply_analyzer()
        if result : sendMSG = self.SUCCESS
        else : sendMSG = self.FAIL

        return self.make_message(user=user, sendMSG=sendMSG, filename=filename)

    def make_message(self, user, sendMSG, filename):
        message = {
            "event": "send",
            "user" : user,
            "textContent": {
                "text": sendMSG + "\n- download link: "
                        + self.make_link(filename=filename)
            }
        }
        return message

    def make_link(self, filename):
        link = "http://localhost:8000/download/"+self.PATH + filename
        return link
