class exception:
    def __init__(self):
        self.error = "서버가 클라이언트의 요청에 응답하는 데 실패하였습니다 :("

    def error(self, user):
        message = {
            "event": "send",
            "user" : user,
            "textContent": {
                "text": self.error
            }
        }
        return message
