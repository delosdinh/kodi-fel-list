# Kodi Dolby Vision FEL Lists

Automatically generated JSON lists of **Dolby Vision Profile 7 FEL movies** for use with Kodi and TMDbHelper.

This repository converts the data from [Appz4Fun's Dolby Vision FEL Movies database](https://github.com/Appz4Fun/fel-dolby-vision-movies) into TMDbHelper-compatible JSON lists that can be used directly as Kodi nodes and widgets.

The lists are automatically updated daily using GitHub Actions.

## Available Lists

### 🗃️ All Dolby Vision Profile 7 FEL Movies

The complete catalogue of confirmed Dolby Vision Profile 7 FEL movies, including both released and upcoming titles.

```text
plugin://plugin.video.themoviedb.helper/?info=mdblist_locallist&&https://raw.githubusercontent.com/delosdinh/kodi-fel-list/main/fel-all.json
```

### 🆕 Latest 50

The **50 most recently released** Dolby Vision Profile 7 FEL movies, sorted by **Blu-ray release date**, with the newest releases first.

```text
plugin://plugin.video.themoviedb.helper/?info=mdblist_locallist&&https://raw.githubusercontent.com/delosdinh/kodi-fel-list/main/fel-latest.json
```

### 📚 FEL Catalogue — Releases 51+

The remaining released Dolby Vision Profile 7 FEL movies, starting from **release 51 onwards**. This list excludes the 50 movies included in the Latest 50 list.

```text
plugin://plugin.video.themoviedb.helper/?info=mdblist_locallist&&https://raw.githubusercontent.com/delosdinh/kodi-fel-list/main/fel-catalogue.json
```

### 🔜 Upcoming FEL Releases

Confirmed Dolby Vision Profile 7 FEL movies with a **future Blu-ray release date**, sorted by the upcoming release date.

```text
plugin://plugin.video.themoviedb.helper/?info=mdblist_locallist&&https://raw.githubusercontent.com/delosdinh/kodi-fel-list/main/fel-upcoming.json
```

## Adding the Lists to Kodi

When adding a widget in Kodi using a compatible skin:

1. Select **TheMovieDb Helper** as the add-on.
2. Select **Node**.
3. Set the node path to one of the URLs above.
4. Save the widget.

TMDbHelper will read the JSON data and populate the widget with the corresponding movies.

## Data Source

The underlying Dolby Vision FEL data is provided by:

**[Appz4Fun – Dolby Vision FEL Movies](https://github.com/Appz4Fun/fel-dolby-vision-movies)**

This repository does not maintain or claim ownership of the underlying Dolby Vision FEL database. It transforms the publicly available data from Appz4Fun into a format suitable for use with TMDbHelper and Kodi.

All credit for the original Dolby Vision FEL research and database goes to **Appz4Fun**.

## Disclaimer

This is an independent community-made utility and is not affiliated with or endorsed by Appz4Fun, TMDb, Kodi, or the developers of TMDbHelper.

The generated lists are dependent on the upstream Appz4Fun database and may change as the source data is updated.

## Updates

The lists are automatically regenerated **daily** using GitHub Actions.

When new Dolby Vision Profile 7 FEL releases are added to the upstream database, the generated Kodi lists will be updated automatically.
