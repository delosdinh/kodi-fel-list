import json
import urllib.request
from datetime import date, datetime

SOURCE_URL = (
    "https://raw.githubusercontent.com/"
    "Appz4Fun/fel-dolby-vision-movies/main/data/releases.json"
)

TODAY = date.today()


def fetch_json(url):
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Kodi-FEL-List/1.0"
        }
    )

    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def parse_date(value):
    if not value:
        return None

    try:
        return datetime.strptime(
            value[:10],
            "%Y-%m-%d"
        ).date()
    except (ValueError, TypeError):
        return None


def convert_movie(movie):
    # Only confirmed FEL releases
    if movie.get("fel_confirmed") is not True:
        return None

    # Movies only
    if movie.get("media_type") != "movie":
        return None

    tmdb_id = movie.get("tmdb_id")

    if not tmdb_id:
        return None

    title = movie.get("movie_title", "").strip()

    if not title:
        return None

    # Physical Blu-ray release date
    bluray_date = parse_date(
        movie.get("bluray_release_date")
    )

    if bluray_date is None:
        return None

    release_year = None

    theatrical_date = parse_date(
        movie.get("release_date")
    )

    if theatrical_date:
        release_year = theatrical_date.year

    item = {
        "id": int(tmdb_id),
        "rank": 0,
        "adult": 0,
        "title": title,
        "imdb_id": movie.get("imdb_id", ""),
        "mediatype": "movie",
    }

    if release_year:
        item["release_year"] = release_year

    return {
        "date": bluray_date,
        "item": item
    }


def save_json(filename, movies):
    items = []

    for rank, movie in enumerate(movies, start=1):
        item = movie["item"].copy()
        item["rank"] = rank
        items.append(item)

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            items,
            file,
            indent=4,
            ensure_ascii=False
        )

    print(
        f"{filename}: {len(items)} movies"
    )


def main():

    data = fetch_json(SOURCE_URL)

    released = []
    upcoming = []

    for movie in data:

        result = convert_movie(movie)

        if result is None:
            continue

        release_date = result["date"]

        if release_date > TODAY:
            upcoming.append(result)
        else:
            released.append(result)

    # ---------------------------------------------------------
    # RELEASED
    # Newest Blu-ray first
    # ---------------------------------------------------------

    released.sort(
        key=lambda x: x["date"],
        reverse=True
    )

    # ---------------------------------------------------------
    # UPCOMING
    # Soonest Blu-ray first
    # ---------------------------------------------------------

    upcoming.sort(
        key=lambda x: x["date"]
    )

    # ---------------------------------------------------------
    # ALL
    # Released + upcoming
    # Newest/most recent date first
    # ---------------------------------------------------------

    all_movies = released + upcoming

    all_movies.sort(
        key=lambda x: x["date"],
        reverse=True
    )

    # ---------------------------------------------------------
    # LATEST 50
    # ---------------------------------------------------------

    latest = released[:50]

    # ---------------------------------------------------------
    # CATALOGUE
    # Everything AFTER latest 50
    # ---------------------------------------------------------

    catalogue = released[50:]

    # ---------------------------------------------------------
    # SAVE
    # ---------------------------------------------------------

    save_json(
        "fel-latest.json",
        latest
    )

    save_json(
        "fel-catalogue.json",
        catalogue
    )

    save_json(
        "fel-upcoming.json",
        upcoming
    )

    save_json(
        "fel-all.json",
        all_movies
    )

    # ---------------------------------------------------------
    # INFORMATION
    # ---------------------------------------------------------

    print()
    print("====================================")
    print("Dolby Vision FEL Lists")
    print("====================================")
    print(
        f"Released FEL movies: {len(released)}"
    )
    print(
        f"Latest 50: {len(latest)}"
    )
    print(
        f"Catalogue after latest 50: {len(catalogue)}"
    )
    print(
        f"Upcoming FEL movies: {len(upcoming)}"
    )
    print(
        f"All FEL movies: {len(all_movies)}"
    )

    if latest:
        print()
        print(
            "Newest released:",
            latest[0]["item"]["title"]
        )

    if upcoming:
        print(
            "Next upcoming:",
            upcoming[0]["item"]["title"]
        )


if __name__ == "__main__":
    main()
