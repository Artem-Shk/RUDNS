import requests
from RutubeParser.CustomTypes.VideoInfo import VideoInfo

import os

class Downloader():
    idVideo = 0
    @classmethod
    def download_img(self, video: VideoInfo):
        id = Downloader.idVideo.__str__()
        raw_name_file = video.image_url.split("/")[-1]
        format = raw_name_file.split('.')[1]
        name_file = raw_name_file.split('.')[0] 

        catalog = video.catalog
      
        if not os.path.exists(
           path_cotalog := f"res_img/{catalog}"
        ):
            os.makedirs(path_cotalog)
        with open(f"res_img/{catalog}/{name_file}_({id}).{format}", "wb") as img:
            img.write(
                requests.get(video.image_url).content
            )
      
        with open(f"res_img/{catalog}/{name_file}_({id})_meta.txt", "w", encoding="utf-8") as metainfo:
            metainfo.write(
                video.prompt
            )
        Downloader.idVideo +=1
            )
