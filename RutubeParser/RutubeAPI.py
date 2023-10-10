import requests
import json
import random
from RutubeParser.CustomTypes.VideoInfo import VideoInfo


class RutubeAPI:

    def __init__(self) -> None:
        self.__category_list_url: str = "https://rutube.ru/api/video/category/?format=json"
        self.__videos_by_category_url: str = "http://rutube.ru/api/video/category/{}/?format=json&page={}"
        self.__info_video_url: str = "http://rutube.ru/api/video/{}/?format=json"
        
        self.__requests_session: requests.Session = requests.Session()

        self.__category_dict: list = []
        self.__get_category_dict()

    def __get_category_dict(self) -> None:
        category_list_response = self.__requests_session.get(self.__category_list_url)
        category_list_json_list = json.loads(category_list_response.content)
        for category in category_list_json_list: self.__category_dict.append(category["id"])

    @classmethod
    def get_info_by_url(self, url_video: str) -> VideoInfo:
        sp = url_video.split("/")
        data =  self.__requests_session.get(
            self.__info_video_url.format(
                sp[-2]
                )
        ).content
        print(sp)
        json_data = json.loads(data)
        
        return VideoInfo(
            title=json_data["title"],
            catalog=json_data["category"]["name"],
            image_url=json_data["thumbnail_url"]
        )
    
    def get_random_video(self) -> VideoInfo: #TODO Оптимизировать метод!
        json_data = json.loads(
            self.__requests_session.get(
                self.__videos_by_category_url.format(
                    random.choice(self.__category_dict),
                    random.choice(range(10))
                )
            ).content
        )
        video = random.choice(json_data["results"])
        return VideoInfo(
            title=video["title"],
            catalog=video["category"]["name"],
            image_url=video["thumbnail_url"]
        ) 

