import os
from nfo import generate_nfo
from tmdb import api, download
from config import API, Language, base_url, poster_sizes, backdrop_sizes, NFOType


def deal_with_movie(movie_file, search_key, language):
    dir_path = os.path.dirname(movie_file)
    info = api(API.movie, search_key, language)
    best_match = info["results"][0]
    download(url=f"{base_url}/{poster_sizes[-1]}{best_match['poster_path']}", save_dir=dir_path)
    download(url=f"{base_url}/{backdrop_sizes[-1]}{best_match['backdrop_path']}", save_dir=dir_path)
    generate_nfo(f_name=f'{movie_file[:movie_file.rfind(".")]}.nfo', nfo_type=NFOType.movie, detail=best_match)


def deal_with_tv(tv_dir_path, search_key, language):
    info = api(API.tv, search_key, language)
    best_match = info["results"][0]
    download(url=f"{base_url}/{poster_sizes[-1]}{best_match['poster_path']}", save_dir=tv_dir_path)
    download(url=f"{base_url}/{backdrop_sizes[-1]}{best_match['backdrop_path']}", save_dir=tv_dir_path)
    generate_nfo(f_name=os.path.join(tv_dir_path, 'tvshow.nfo'), nfo_type=NFOType.movie, detail=best_match)
    for root, dirs, files in os.walk(tv_dir_path):
        for file_name in files:
            if any([file_name.endswith(media_suffix) for media_suffix in [".mkv", ".mp4"]]):
                best_match["title"] = file_name[:file_name.rfind(".")]
                deal_with_episode(os.path.join(root, best_match["title"]), best_match)


def deal_with_episode(episode_file, info):
    generate_nfo(f_name=f'{episode_file}.nfo', nfo_type=NFOType.episode, detail=info)


if __name__ == "__main__":
    # deal_with_movie(movie_file=r"E:\aliyun\新建文件夹\test\[BeanSub&FZSD][Jigokuraku][11][GB][1080P][x264_AAC].mp4", search_key="阿甘正传", language=Language.zh)
    deal_with_tv(tv_dir_path=r"E:\aliyun\新建文件夹", search_key="地狱乐", language=Language.zh)
    # import sys
    # from optparse import OptionParser

    # optParser = OptionParser()
    # optParser.add_option('-l', '--language', type="string", dest='language')
    # optParser.add_option("-n", "--name", type="string", dest="name")
    # optParser.add_option("-s", "--search_key", type="string", dest="search_key")
    # optParser.add_option("-t", "--type", type="string", dest="type")
    # opts, args = optParser.parse_args(sys.argv)

    # if "en" in opts.language:
    #     lan = Language.en
    # else:
    #     lan = Language.zh

    # if opts.type == "movie":
    #     deal_with_movie(movie_file=opts.name, search_key=opts.search_key, language=lan)
    # elif opts.type == "tv" or opts.type == "anime":
    #     deal_with_tv(tv_dir_path=opts.name, search_key=opts.search_key, language=lan)
