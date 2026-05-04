class Card:
    def __init__(self, website_name="", website_url="", login_name="", login="", password="", comment=""):
        self.website_name = website_name
        self.website_url = website_url
        self.login_name = login_name
        self.login = login
        self.password = password
        self.comment = comment

    def to_dict(self):
        return {
            "website_name": self.website_name,
            "website_url": self.website_url,
            "login_name": self.login_name,
            "login": self.login,
            "password": self.password,
            "comment": self.comment
        }

    @staticmethod
    def from_dict(data):
        return Card(
            website_name=data.get("website_name", ""),
            website_url=data.get("website_url", ""),
            login_name=data.get("login_name", ""),
            login=data.get("login", ""),
            password=data.get("password", ""),
            comment=data.get("comment", "")
        )