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
        headers={"User-Agent": "Kodi-FEL-List/1.0"}
    )

    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def parse_date(value):
    if not value:
        return None

    if isinstance(value, str):
        value = value.strip()

        # Try YYYY-MM-DD
        try:
            return datetime.strptime(value[:10], "%Y-%m-%d").date()
        except ValueError:
            pass

        # Try DD/MM/YYYY
        try:
            return datetime.strptime(value[:10], "%d/%m/%Y").date()
        except ValueError:
            pass

        # Try MM/DD/YYYY
        try:
            return datetime.strptime(value[:10], "%m/%d/%Y").date()
        except ValueError:
            pass

    return None


def convert_movie(movie):
    if movie.get("fel_confirmed") is not True:
        return None

    if movie.get("media_type") != "movie":
        return None

    tmdb_id = movie.get("tmdb_id")

    if not tmdb_id:
        return None

    title = movie.get("movie_title", "").strip()

    if not title:
        return None

    bluray_date = parse_date(movie.get("bluray_release_date"))

    if bluray_date is None:
        return None

    release_year = None

    theatrical_date = parse_date(movie.get("release_date"))

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

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(
            items,
            file,
            indent=4,
            ensure_ascii=False
        )

    print(f"{filename}: {len(items)} movies")


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

    # Newest Blu-ray releases first
    released.sort(
        key=lambda x: x["date"],
        reverse=True
    )

    # Upcoming releases soonest first
    upcoming.sort(
        key=lambda x: x["date"]
    )

    # Complete master list
    all_movies = released + upcoming

    # Latest 50
    latest = released[:50]

    # Everything after the latest 50
    catalogue = released[50:]

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

    print()
    print("====================================")
    print("Dolby Vision FEL Lists")
    print("====================================")

    print(f"Released FEL movies: {len(released)}")
    print(f"Latest 50: {len(latest)}")
    print(f"Catalogue after latest 50: {len(catalogue)}")
    print(f"Upcoming FEL movies: {len(upcoming)}")
    print(f"All FEL movies: {len(all_movies)}")

    print()
    print("10 newest released FEL movies:")

    for movie in released[:10]:
        print(
            f"{movie['date']} - "
            f"{movie['item']['title']}"
        )

    print()

    if upcoming:
        print(
            "Next upcoming:",
            upcoming[0]["date"],
            "-",
            upcoming[0]["item"]["title"]
        )


if __name__ == "__main__":
    main()
