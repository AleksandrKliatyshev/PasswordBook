import yadisk
import json
import os
from models import Card

class YandexStorage:
    def __init__(self, token_write, token_read, dir_path="/PasswordBook/"):
        self.dir_path = dir_path
        self.file_path = dir_path + "data.json"
        self.y_write = yadisk.YaDisk(token=token_write)
        self.y_read = yadisk.YaDisk(token=token_read)
        try:
            self.y_write.mkdir(dir_path)
        except:
            pass

    def download(self):
        try:
            self.y_read.download(self.file_path, "data.json")
            return True
        except:
            return False

    def upload(self):
        if os.path.exists("data.json"):
            try:
                self.y_write.upload("data.json", self.file_path, overwrite=True)
                return True
            except:
                return False
        return False

    def load_cards(self):
        if os.path.exists("data.json"):
            with open("data.json", "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    return [Card.from_dict(item) for item in data]
                except:
                    return []
        return []

    def save_cards(self, cards):
        data = [card.to_dict() for card in cards]
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        self.upload()