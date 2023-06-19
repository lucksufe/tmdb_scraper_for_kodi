import json

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwYWJlODA4YzE1ZmRlMmJiNWZkNWFlZWE2MzE2NTgyMyIsInN1YiI6IjY0OGZhYTk4MmY4ZDA5MDEzYWZhYjJmMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.eeQnLbLRrjqA-HNeKFpId-KVz9_VW4yDMIh-E2wzC2c"
}


class NFOType:
    movie = "movie"
    tv = "tvshow"
    episode = "episodedetails"


class API:
    tv = "tv"
    movie = "movie"


class Language:
    en = "en-US"
    zh = "zh-CN"


w600_and_h900 = "w600_and_h900_bestv2"

with open("image.json", "r", encoding="utf-8") as f:
    image_json = json.load(f)
    base_url = image_json["images"]["base_url"]
    poster_sizes = image_json["images"]["poster_sizes"]
    backdrop_sizes = image_json["images"]["backdrop_sizes"]

genre_map = {}

with open("genre_tv_en.json", "r", encoding="utf-8") as f:
    genre_tv_en = {item["id"]: item["name"] for item in json.load(f)["genres"]}
    genre_map[f"{API.tv}_{Language.en}"] = genre_tv_en

with open("genre_tv_zh.json", "r", encoding="utf-8") as f:
    genre_tv_zh = {item["id"]: item["name"] for item in json.load(f)["genres"]}
    genre_map[f"{API.tv}_{Language.zh}"] = genre_tv_zh

with open("genre_movie_en.json", "r", encoding="utf-8") as f:
    genre_movie_en = {item["id"]: item["name"] for item in json.load(f)["genres"]}
    genre_map[f"{API.movie}_{Language.en}"] = genre_movie_en

with open("genre_movie_zh.json", "r", encoding="utf-8") as f:
    genre_movie_zh = {item["id"]: item["name"] for item in json.load(f)["genres"]}
    genre_map[f"{API.movie}_{Language.zh}"] = genre_movie_zh
