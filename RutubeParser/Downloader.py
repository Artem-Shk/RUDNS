import requests
from .CustomTypes.VideoInfo import VideoInfo

import os

class Downloader():
    @classmethod
    def download_img(self, video: VideoInfo):
        name_file = video.image_url.split("/")[-1]
        catalog = video.catalog
        if not os.path.exists(
           path_cotalog := f"res_img/{catalog}"
        ):
            os.makedirs(path_cotalog)
   
        
        with open(f"res_img/{catalog}/{name_file}", "wb") as img:
            img.write(
                requests.get(video.image_url).content
            )
        with open(f"res_img/{catalog}/{name_file}_meta.txt", "w", encoding="utf-8") as metainfo:
            metainfo.write(
                video.prompt
            )