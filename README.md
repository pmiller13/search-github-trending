# Trending GitHub Repository Archive
Welcome to the Trending GitHub Repository Archive - a simple and sleek single-page interface designed to explore and search through a curated collection of GitHub repositories that have trended over time.

![Demo](./demo.gif)

## Features
- **Fast Search**: Instantly search over 40,000 GitHub repos that have trended over time using a reverse index keyword based search engine.
- **Compact**: Simply open the index.html and accompanying data.json that powers the search engine.
- **Minimal Dependencies**: Setup only requires Python and Javascript standard libraries.
- **Easily Self Host**: Easily recreate the site for yourself.

## How does it work?
As of today this project is made possible by 3 steps:
1. Clone this GitHub repo containing daily trending GitHub repos https://github.com/larsbijl/trending_archive.
2. Transform the historic repo files into a `data.json` following this schema:
```json
{
    {
        "<repository_url>": {
            "body": "string",
            "date": "date",
            "dates": [
            "date"
            ],
            "searchable": "string",
            "title": "string",
            "url": "string"
        }
    },
    ....
}
```

- `<repository_url>`: String representing the URL of the GitHub repository.
- `body`: String containing the description or body of the repository.
- `date`: Date string (in "YYYY-MM-DD" format), representing the latest time the GitHub repository was trending.
- `dates`: An array of date strings (each in "YYYY-MM-DD" format), representing the historical dates when the GitHub repository was trending.
- `searchable`: String derived from the `body` field, transformed and normalized to be more search-friendly.
- `title`: String representing the title of the repository.
- `url`: String representing the URL of the repository. This is the same as `<repository_url>`.
 

3. Make `data.json` searchable via reverse index keyword searching with a frontend.

## Deployment
To "just make this work", please simply run the following:
```
git clone https://github.com/larsbijl/trending_archive.git
python transform_trending_archive.py
open index.html   # Open in favorite web browser
```