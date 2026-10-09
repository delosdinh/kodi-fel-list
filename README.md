
# Kodi Dolby Vision FEL Lists

Automatically generated JSON lists of **Dolby Vision Profile 7 FEL movies** for use with Kodi, TMDbHelper, AIOMetadata and compatible Stremio-based apps.

This repository converts the data from [Appz4Fun's Dolby Vision FEL Movies database](https://github.com/Appz4Fun/fel-dolby-vision-movies) into TMDbHelper-compatible JSON lists and provides a Stremio-compatible catalogue add-on for browsing FEL movies through supported apps.

The lists are automatically updated daily using GitHub Actions.

## Available Lists

### 🗃️ All Dolby Vision Profile 7 FEL Movies

The complete catalogue of confirmed Dolby Vision Profile 7 FEL movies, including released and upcoming titles.

**TMDbHelper node path:**

```text
plugin://plugin.video.themoviedb.helper/?info=mdblist_locallist&&https://raw.githubusercontent.com/delosdinh/kodi-fel-list/main/fel-all.json
```

**Direct JSON:** [fel-all.json](https://raw.githubusercontent.com/delosdinh/kodi-fel-list/main/fel-all.json)

### 🆕 Latest 50

The 50 most recently released Dolby Vision Profile 7 FEL movies, sorted by Blu-ray release date, newest first.

**TMDbHelper node path:**

```text
plugin://plugin.video.themoviedb.helper/?info=mdblist_locallist&&https://raw.githubusercontent.com/delosdinh/kodi-fel-list/main/fel-latest.json
```

**Direct JSON:** [fel-latest.json](https://raw.githubusercontent.com/delosdinh/kodi-fel-list/main/fel-latest.json)

### 📚 FEL Catalogue — Releases 51+

The remaining released Dolby Vision Profile 7 FEL movies, starting from release 51 onwards. This list excludes the 50 movies included in Latest 50.

**TMDbHelper node path:**

```text
plugin://plugin.video.themoviedb.helper/?info=mdblist_locallist&&https://raw.githubusercontent.com/delosdinh/kodi-fel-list/main/fel-catalogue.json
```

**Direct JSON:** [fel-catalogue.json](https://raw.githubusercontent.com/delosdinh/kodi-fel-list/main/fel-catalogue.json)

### 🔜 Upcoming FEL Releases

Confirmed Dolby Vision Profile 7 FEL movies with a future Blu-ray release date, sorted by upcoming release date.

**TMDbHelper node path:**

```text
plugin://plugin.video.themoviedb.helper/?info=mdblist_locallist&&https://raw.githubusercontent.com/delosdinh/kodi-fel-list/main/fel-upcoming.json
```

**Direct JSON:** [fel-upcoming.json](https://raw.githubusercontent.com/delosdinh/kodi-fel-list/main/fel-upcoming.json)

## Using the FEL Catalogue with AIOMetadata and Nuvio

A Stremio-compatible catalogue add-on is available for browsing the FEL lists in supported apps, including setups that use AIOMetadata and Nuvio.

### Add the FEL Catalogue

**Manifest URL:**

https://fel-catalogue.delos-dinh.workers.dev/manifest.json

1. Open your AIOMetadata configuration.
2. Navigate to the **Catalogs** section.
3. Choose the option to add an external or custom catalogue/add-on.
4. Enter the manifest URL above.
5. Save or confirm the addition.
6. Refresh or reload your catalogues if necessary.
7. Open Nuvio and check the available catalogues.

The add-on exposes four catalogues:

- **Latest 50 FEL Movies**
- **FEL Catalogue**
- **Upcoming FEL Releases**
- **All FEL Movies**

The add-on reads the JSON lists hosted in this repository and converts the movie entries into a Stremio-compatible catalogue format.

**Note:** Catalogue visibility depends on the app and its integration with AIOMetadata. The add-on provides movie metadata and browsing, not video streams. Use your existing authorised streaming or local-media providers for playback.

### Test the Add-on

You can check the manifest and individual catalogue endpoints in a web browser:

- [Add-on manifest](https://fel-catalogue.delos-dinh.workers.dev/manifest.json)
- [Latest 50 catalogue](https://fel-catalogue.delos-dinh.workers.dev/catalog/movie/fel-latest.json)
- [FEL Catalogue](https://fel-catalogue.delos-dinh.workers.dev/catalog/movie/fel-catalogue.json)
- [Upcoming FEL Releases](https://fel-catalogue.delos-dinh.workers.dev/catalog/movie/fel-upcoming.json)
- [All FEL Movies](https://fel-catalogue.delos-dinh.workers.dev/catalog/movie/fel-all.json)

## Adding the Lists to Kodi with TMDbHelper

For Kodi skins that support TMDbHelper widgets:

1. Select **TheMovieDb Helper** as the add-on.
2. Select **Node**.
3. Set the node path to one of the TMDbHelper URLs listed above.
4. Save the widget.

TMDbHelper will read the JSON data and populate the widget with the corresponding movies.

## Data Source

The underlying Dolby Vision FEL data is provided by:

**[Appz4Fun – Dolby Vision FEL Movies](https://github.com/Appz4Fun/fel-dolby-vision-movies)**

This repository does not maintain or claim ownership of the underlying Dolby Vision FEL database. It transforms publicly available data from Appz4Fun into a format suitable for TMDbHelper and Kodi, and provides a compatible catalogue endpoint for supported apps.

All credit for the original Dolby Vision FEL research and database goes to **Appz4Fun**.

## Disclaimer

This is an independent community-made utility and is not affiliated with or endorsed by Appz4Fun, TMDb, Kodi, TMDbHelper, AIOMetadata, Nuvio or Cloudflare.

The generated lists depend on the upstream Appz4Fun database and may change as the source data is updated. Catalogue availability also depends on the third-party services used to host and display the lists.

## Updates

The JSON lists are automatically regenerated daily using GitHub Actions.

When new Dolby Vision Profile 7 FEL releases are added to the upstream database, the generated Kodi lists will be updated automatically. The catalogue add-on reads the hosted JSON files, so its catalogue contents follow those updates without requiring users to reinstall the add-on.
