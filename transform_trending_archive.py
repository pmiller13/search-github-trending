import glob
import re
import json
from datetime import datetime
from body_transform import transform_body

DATA_FILE = "data.json"


def transform_md_files():
    data = {}

    magic_pattern = r"\* \[(.*)\]\((.*)\):([ ].*)\n"
    date_pattern = r"(\d{4}-\d{1,2}-\d{1,2})"
    for fp in glob.glob("./trending_archive/**/[0-9]*.md", recursive=True):
        with open(fp, "r") as f:
            file_data = f.read()
            matches = re.findall(magic_pattern, file_data)
            date_match = re.search(date_pattern, fp)
            if not date_match:
                continue
            date_match = date_match.group(1)
            for i, match in enumerate(matches):
                try:
                    title_match = match[0]
                    url_match = match[1]
                    body_match = match[2]
                except Exception:
                    print(fp)
                    print(file_data)
                    continue

                transformed_body = transform_body(body_match)
                entry = {
                    "title": title_match,
                    "url": url_match,
                    "searchable": transformed_body,
                    "body": body_match,
                    "date": date_match
                }

                if url_match not in data:
                    data[url_match] = entry
                    data[url_match]['dates'] = [date_match]
                elif url_match in data and datetime.strptime(
                    date_match, "%Y-%m-%d"
                ) > datetime.strptime(data[url_match]['date'], "%Y-%m-%d"):
                    data[url_match]['date'] = date_match
                    data[url_match]['dates'].append(date_match)
    with open(DATA_FILE, "w") as f:
        f.write(json.dumps(data, sort_keys=True, indent=1, separators=(",", ":")))

    return data


if __name__ == "__main__":
    results = transform_md_files()


