import json
from datetime import datetime


class Message:
    def __init__(self, content, user):
        self.content: str = content
        self.user: str = user
        self.time: str = self.getTime()

    def getTime(self):
        time = datetime.now()
        return time.strftime("%H:%M:%S")

    def toJSON(self):
        return json.dumps(self.__dict__)
