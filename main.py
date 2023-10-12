from progress.bar import ShadyBar
from pprint import pprint

if __name__ == "__main__":
    from RutubeParser.RutubeAPI import RutubeAPI
    from RutubeParser.Downloader import Downloader

    parser = RutubeAPI()
    print(parser.get_video_by_autor("23337407"))
    
    # with open("tests_urls.txt", "r") as file:
    #     urls = file.readlines()
    #     bar = ShadyBar("Downoload", max=len(urls))
    #     for i in urls:
    #        Downloader.download_img(parser.get_info_by_url(i))
    #        bar.next()
    #     bar.finish()