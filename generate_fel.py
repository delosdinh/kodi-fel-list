import json
import urllib.request
from datetime import date

SOURCE_URL = (
    "https://raw.githubusercontent.com/"
    "Appz4Fun/fel-dolby-vision-movies/main/data/releases.json"
)

TODAY = date.today().isoformat()


def fetch_json(url):
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Kodi-FEL-List/1.0"}
    )

    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def convert_movie(movie, rank):
    tmdb_id = movie.get("tmdb_id")

    if not tmdb_id:
        return None

    title = movie.get("movie_title", "").strip()

    if not title:
        return None

    bluray_date = movie.get("bluray_release_date")

    # Only include titles that actually have a Blu-ray date.
    if not bluray_date:
        return None

    # Do not show future releases in the "latest releases" widget.
    if bluray_date > TODAY:
        return None

    release_year = None

    release_date = movie.get("release_date")
    if release_date and len(release_date) >= 4:
        try:
            release_year = int(release_date[:4])
        except ValueError:
            pass

    item = {
        "id": int(tmdb_id),
        "rank": rank,
        "adult": 0,
        "title": title,
        "imdb_id": movie.get("imdb_id", ""),
        "mediatype": "movie",
    }

    if release_year:
        item["release_year"] = release_year

    return item


def main():
    data = fetch_json(SOURCE_URL)

    movies = []

    for movie in data:
        if not movie.get("fel_confirmed"):
            continue

        if movie.get("media_type") != "movie":
            continue

        item = convert_movie(movie, 0)

        if item:
            movies.append((movie.get("bluray_release_date"), item))

    # Newest UHD/Blu-ray releases first.
    movies.sort(
        key=lambda x: x[0],
        reverse=True
    )

    # Generate the complete list.
    all_items = []

    for index, (_, item) in enumerate(movies, start=1):
        item["rank"] = index
        all_items.append(item)

    # Generate a smaller "latest" list.
    latest_items = all_items[:50]

    with open("fel-all.json", "w", encoding="utf-8") as file:
        json.dump(
            all_items,
            file,
            indent=4,
            ensure_ascii=False
        )

    with open("fel-latest.json", "w", encoding="utf-8") as file:
        json.dump(
            latest_items,
            file,
            indent=4,
            ensure_ascii=False
        )

    print(f"Generated {len(all_items)} FEL movies.")
    print(f"Latest list contains {len(latest_items)} movies.")


if __name__ == "__main__":
    main()
