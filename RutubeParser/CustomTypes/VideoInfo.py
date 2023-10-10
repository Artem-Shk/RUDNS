import requests as req
from io import StringIO

class VideoInfo:
    def __init__(self, title: str, catalog: str, image_url: str):
        self.title = title
        self.catalog = catalog
        self.image_url = image_url

    @property
    def prompt(self) -> str:
        return f"#Preview {self.catalog} {self.title}"

    @property
    def image(self) -> StringIO:
        return StringIO(req.get(self.image_url).content)