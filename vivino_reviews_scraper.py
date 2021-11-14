"""
    Module for scraping vivino.com for wine information
"""

import time
import requests
import pandas as pd
from progress.bar import Bar

REVIEWS_PER_WINE = 15
REVIEW_LANGUAGE = 'en'
INFO_FILE = 'datasets/vivino-info.csv'
REVIEW_FILE = 'datasets/vivino-reviews.csv'
REVIEW_COLUMNS = ['vivino_id', 'rating', 'note', 'user']

def persistent_request(url, parameters, max_retries):
    """Retry get request on failure """
    retries = 1
    while True:
        try:
            request = requests.get(url, params = parameters,
                headers= {
                    "User-Agent":
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"
                }
            )
            return request
        except Exception:
            if retries > max_retries:
                print('Aborted: connection failed too many times in a row')
                exit()
            time.sleep(retries)
            retries += 1

def get_wine_reviews(wine_id, year, page):
    """Get reviews for a specific wine  """

    url =  f"https://www.vivino.com/api/wines/{wine_id}/reviews?per_page={REVIEWS_PER_WINE}&year={year}&page={page}"
    return persistent_request(url, None, 20)

df = pd.read_csv(INFO_FILE)

# Scraping the reviews from Vivino
bar = Bar('Scraping reviews from vivino.com, this may take several minutes', max=df.shape[0])
reviews = []

for _, row in df.iterrows():
    bar.next()

    data = get_wine_reviews(row["vivino_id"], row["year"], 1).json()

    if not data["reviews"]:
        continue

    for r in data["reviews"]:
        if r["language"] != REVIEW_LANGUAGE:
            continue

        reviews.append(
            [
                row["vivino_id"],
                r["rating"],
                r["note"].replace('\n', ' '),
                r["user"]["alias"]
            ]
        )


bar.finish()

dfr = pd.DataFrame(reviews, columns=REVIEW_COLUMNS)

dfr.to_csv(REVIEW_FILE, index=False)
print(f'Wine review dataset written to {REVIEW_FILE}')
