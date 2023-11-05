class Post:
    def __init__(self, id: str, title: str, subtitle: str, content: str) -> None:
        self.id = int(id)
        self.title = title
        self.subtitle = subtitle
        self.content = content

    def get_url(self):
        return "/post/" + str(self.id)
