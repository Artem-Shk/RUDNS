class VideInfo:
    def __init__(self, title: str, catalog: str, image_url: str):
        self.title = title
        self.catalog = catalog
        self.image_url = image_url

    @property
    def prompt(self) -> str:
        return f"{self.catalog} {self.title}".lower()

    # TODO image loader to narray
    @property
    def image(self) -> list:
        ...