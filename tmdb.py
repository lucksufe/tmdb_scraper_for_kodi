import os
import requests
from config import API, Language, headers, genre_map


def api(api_type: any([API.tv, API.movie]), search_key: str, language: any([Language.en, Language.zh]) = Language.zh) -> dict:
    url = f"https://api.themoviedb.org/3/search/{api_type}?query={search_key}&include_adult=false&language={language}zh-CN&page=1"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        info = response.json()
        info["genre"] = get_genre_str(info.get("genre_ids"), api_type, language)
        return info
    return {}


def get_genre_str(genre_ids: list[int], api_type: any([API.tv, API.movie]), language: any([Language.en, Language.zh])) -> str:
    current_map = genre_map[f"{api_type}_{language}"]
    return "&".join([current_map.get(g_id, str(g_id)) for g_id in genre_ids])


def download(url: str, save_dir: str, rename: str = None) -> None:
    response = requests.get(url)
    pic_name = rename if rename else url[url.rfind("/") + 1:]
    if response.status_code == 200:
        with open(os.path.join(save_dir, pic_name), "wb") as pic:
            pic.write(response.content)
