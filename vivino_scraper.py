"""
    Module for scraping vivino.com for wine information
"""

import time
import requests
import pandas as pd
from progress.bar import Bar

REVIEW_PAGES = 1 # Limits the amount of review pages per wine, each review page has 50 reviews
REVIEW_LANGUAGE = 'en'
INFO_FILE = 'datasets/vivino-info.csv'
REVIEW_FILE = 'datasets/vivino-reviews.csv'
ITEMS_PER_PAGE = 24
INFO_COLUMNS = ['vivino_id', 'winery', 'year', 'name', 'type',
            'rating', 'price', 'country', 'region', 'image_url']
REVIEW_COLUMNS = ['vivino_id', 'rating', 'note', 'user']

def get_type_name(type_id):
    """ Since wine type comes as an id, convert to the corresponding name """

    if type_id == 1:
        return 'red'
    if type_id == 2:
        return 'white'
    if type_id == 3:
        return 'sparkling'
    if type_id == 4:
        return 'rosé'
    if type_id == 5:
        return 'dessert'
    if type_id == 6:
        return 'fortified'

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


def get_page(page, country_codes = 'pt'):
    """Get 24 item page from vivino.com """

    url =   "https://www.vivino.com/api/explore/explore"
    params = {
                "country_code": "PT",
                "country_codes[]":country_codes,
                "currency_code":"EUR",
                "grape_filter":"varietal",
                "min_rating":"1",
                "order_by":"price",
                "order":"asc",
                "page": page,
            }
    return persistent_request(url, params, 20)


def get_result_count(country_codes = 'pt'):
    """Get total count of matches for a country search  """

    results_matched = get_page(1, country_codes).json()['explore_vintage']['records_matched']
    return results_matched


def get_wine_reviews(wine_id, year, page):
    """Get reviews for a specific wine  """

    url =  f"https://www.vivino.com/api/wines/{wine_id}/reviews?per_page=50&year={year}&page={page}"
    return persistent_request(url, None, 20)


result_count = get_result_count() # Get portuguese wine count
total_pages = result_count // ITEMS_PER_PAGE + 1 # Amount of pages of portuguese wine
data = []

# begin scraping and cataloguing data
bar = Bar('Scraping wine info pages from vivino.com', max=total_pages)
for i in range(total_pages):
    r = get_page(i)
    bar.next()
    try:
        results = [
            (
                t["vintage"]["wine"]["id"],
                t["vintage"]["wine"]["winery"]["name"],
                t["vintage"]["year"],
                t["vintage"]["name"],
                get_type_name(t["vintage"]["wine"]["type_id"]),
                t["vintage"]["statistics"]["ratings_average"],
                t["price"]["amount"],
                t["vintage"]["wine"]["region"]["country"]["name"],
                t["vintage"]["wine"]["region"]["name"],
                t["vintage"]["image"]["location"]
            )
            for t in r.json()["explore_vintage"]["matches"]
        ]
        data += results
    except TypeError:
        continue

bar.finish()

# save to csv file
df = pd.DataFrame(data, columns=INFO_COLUMNS)
df.to_csv(INFO_FILE)
print(f'Wine info dataset written to {INFO_FILE}')

# Scraping the reviews from Vivino
bar = Bar('Scraping reviews from vivino.com, this may take several minutes', max=df.shape[0])
reviews = []

for _, row in df.iterrows():
    PAGE = 1
    bar.next()
    while True:
        data = get_wine_reviews(row["vivino_id"], row["year"], PAGE).json()

        if not data["reviews"]:
            break

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

        PAGE += 1
        if PAGE > REVIEW_PAGES:
            break

bar.finish()

dfr = pd.DataFrame(reviews, columns=REVIEW_COLUMNS)

dfr.to_csv(REVIEW_FILE)
print(f'Wine review dataset written to {REVIEW_FILE}')
