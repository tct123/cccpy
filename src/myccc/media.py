import requests

BASE_URL = "https://media.ccc.de/public/"
LIVE_URL = "https://streaming.media.ccc.de/streams/v2.json"
RELIVE_URL = "https://cdn.c3voc.de/relive/index.json"


class Media:
    def __init__(self, url="https://api.media.ccc.de/public/recordings/"):
        self.url = url
        self.r = requests.get(url=url)
        self.data = self.r.json()["recordings"]

    def get_media(self):  # mime_type
        media = self.data
        for i in self.data:
            if bool(i["high_quality"]):
                print(i["recording_url"])
        # print(media)


if __name__ == "__main__":
    obj = Media()
    obj.get_media()
