from xml.etree import ElementTree as et
import xml.dom.minidom as minidom
from config import NFOType


def generate_nfo(f_name: str, nfo_type: any([NFOType.movie, NFOType.tv, NFOType.episode]), detail: dict) -> None:
    root = et.Element(nfo_type)

    title = et.SubElement(root, 'title')
    title.text = detail.get("title") if nfo_type == NFOType.movie else detail.get("name")

    unique_id = et.SubElement(root, 'uniqueid')
    unique_id.text = str(detail.get("id"))
    unique_id.set("type", "tmdb")
    unique_id.set("default", "true")

    original_title = et.SubElement(root, 'originaltitle')
    original_title.text = detail.get("original_title") if nfo_type == NFOType.movie else detail.get("original_name")

    plot = et.SubElement(root, 'plot')
    plot.text = detail.get("overview")

    genre_str_list = detail.get("genre").split("&")
    for genre_str in genre_str_list:
        genre = et.SubElement(root, 'genre')
        genre.text = genre_str

    premiered = et.SubElement(root, 'premiered')
    premiered.text = detail.get("release_date") if nfo_type == NFOType.movie else detail.get("first_air_date")

    country = et.SubElement(root, 'country')
    country.text = detail.get("original_language")

    ratings = f'<ratings><rating name="themoviedb" max="10" default="true"><value>{detail.get("vote_average")}</value><votes>{detail.get("vote_count")}</votes></rating></ratings>'
    ratings = et.fromstring(ratings)
    root.append(ratings)

    if detail.get("backdrop_path"):
        landscape = f'<thumb aspect="landscape">{detail.get("backdrop_path")[1:]}</thumb>'
        landscape = et.fromstring(landscape)
        root.append(landscape)
        
        fanart = f'<thumb aspect="fanart">{detail.get("backdrop_path")[1:]}</thumb>'
        fanart = et.fromstring(fanart)
        root.append(fanart)

    if detail.get("poster_path"):
        poster = f'<thumb aspect="poster">{detail.get("poster_path")[1:]}</thumb>'
        poster = et.fromstring(poster)
        root.append(poster)

    popularity = et.SubElement(root, 'popularity')
    popularity.text = str(detail.get("popularity"))

    et.ElementTree(root)
    rough_str = et.tostring(root, 'utf-8')
    parse_and_save(rough_str, f_name)


def parse_and_save(raw: str, f_name: str) -> None:
    parsed = minidom.parseString(raw)
    new_str = parsed.toprettyxml(indent='\t')
    f = open(f_name, 'w', encoding='utf-8')
    f.write(new_str)
    f.close()
