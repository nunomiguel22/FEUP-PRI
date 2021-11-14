"""
    Module for scraping vivino.com for wine information
"""

import time
import requests
import pandas as pd
from progress.bar import Bar


INFO_FILE = 'datasets/vivino-info.csv'
ITEMS_PER_PAGE = 24
INFO_COLUMNS = ['vivino_id', 'winery', 'year', 'name', 'type',
            'rating', 'price', 'country', 'region', 'image_url']

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
    if type_id == 7:
        return 'dessert'
    if type_id == 24:
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



result_count = get_result_count() # Get portuguese wine count
total_pages = result_count // ITEMS_PER_PAGE + 1 # Amount of pages of portuguese wine
data = []

# begin scraping and cataloguing data
bar = Bar('Scraping wine info pages from vivino.com', max=total_pages)
for i in range(total_pages):
    page_request = get_page(i)
    bar.next()

    for match in page_request.json()["explore_vintage"]["matches"]:
        try:
            results = [
                (
                    match["vintage"]["wine"]["id"],
                    match["vintage"]["wine"]["winery"]["name"],
                    match["vintage"]["year"],
                    match["vintage"]["name"],
                    get_type_name(match["vintage"]["wine"]["type_id"]),
                    match["vintage"]["statistics"]["ratings_average"],
                    match["price"]["amount"],
                    match["vintage"]["wine"]["region"]["country"]["name"],
                    match["vintage"]["wine"]["region"]["name"],
                    match["vintage"]["image"]["location"],
                )
            ]
            data += results
        except TypeError:
            continue

bar.finish()

# save to csv file
df = pd.DataFrame(data, columns=INFO_COLUMNS)

print('Checking for and removing duplicates')
df = df.drop_duplicates(subset=['vivino_id', 'year'])

print('Removing rows with incomplete data')
df = df[df['year'] != 'N.V.']


df.to_csv(INFO_FILE, index=False)
print(f'Wine info dataset written to {INFO_FILE}')
