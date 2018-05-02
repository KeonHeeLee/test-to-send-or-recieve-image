SERVER_ERROR = 0
NON_EXISTENT_FILE = 1

class exception:
    def __init__(self):
        self.error = "서버가 클라이언트의 요청에 응답하는 데 실패하였습니다 :("
        self.IS_NOT_FILE = "요청하신 파일이 없습니다 :("

    def error(self, user, flag):
        message = {
            "event": "send",
            "user" : user,
            "textContent": {
                "text": self.error
            }
        }
        return message

    def error_nonfile(self,flag):
        message = {
            "event": "send",
            "user" : "server",
            "textContent": {
                "text": self.IS_NOT_FILE
            }
        }
        return message
