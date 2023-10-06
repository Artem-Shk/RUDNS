import requests
import json
from pprint import pprint
import random


class RutubeAPI:

    def __init__(self) -> None:
        self.__category_list_url : str = "https://rutube.ru/api/video/category/?format=json"
        self.__videos_by_category_url : str = "http://rutube.ru/api/video/category/{}/?format=json&page={}"
        self.__requests_session : requests.Session = requests.Session()
        
        self.__category_dict : list = []
        self.__get_category_dict()

    def __get_category_dict(self) -> None:
        category_list_respons = self.__requests_session.get(self.__category_list_url)
        category_list_json_list = json.loads(category_list_respons.content)
        for category in category_list_json_list: self.__category_dict.append(category["id"]) 
        
    
    def get_random_video(self):        
        json_data = json.loads(
            self.__requests_session.get(
                self.__videos_by_category_url.format(
                        random.choice(self.__category_dict), 
                        random.choice(range(10))
                    )
                ).content
            )
        video = random.choice(json_data["results"])
        return {
                        "title": video["title"],
                        "tag": video["category"]["name"],
                        "img_url": video["thumbnail_url"]
                    }
        


if __name__ == "__main__":

    
    
    api = RutubeAPI()
    for i in range(1000): pprint(
        api.get_random_video()
        )
    