# import argparse
# parser = argparse.ArgumentParser(description='PreView Generator')

# parser.add_argument(
#     "prompt",
#     help="Запрос для генерации",
#     type=str
# )

# parser.add_argument(
#     "--count",
#     default=1,
#     type=int,
#     help="Количество генерируемых картинок"
# )

# args = parser.parse_args()


if __name__ == "__main__":
    from RutubeParser.RutubeAPI import RutubeAPI
    from RutubeParser.Downloader import Downloader
    
    print("Init")
    parser = RutubeAPI()
    
    with open("tests_urls.txt", "r") as file:
        for i in file.readlines():
           Downloader.download_img(
               parser.get_info_by_url(i)
               )