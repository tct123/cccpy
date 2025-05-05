import requests

BASE_URL = "https://media.ccc.de/public/"
LIVE_URL = "https://streaming.media.ccc.de/streams/v2.json"
RELIVE_URL = "https://cdn.c3voc.de/relive/index.json"


class Media:
    def __init__(self, url="https://api.media.ccc.de/public/recordings/"):
        self.url = url
        self.r = requests.get(url=url)
        self.data = self.r.json()["recordings"]
        print(self.data)


if __name__ == "__main__":
    obj = Media()
