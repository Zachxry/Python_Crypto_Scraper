from bs4 import BeautifulSoup
import requests
import pprint
from datetime import datetime
from contextlib import redirect_stdout

# Date information
date_and_time = datetime.now()
dt_string = date_and_time.strftime("%m/%d/%Y %H:%M:%S")

# web scrape for coinmarketcap
url = 'https://coinmarketcap.com/'
result = requests.get(url).text
doc = BeautifulSoup(result, 'html.parser')

tbody = doc.tbody
trs = tbody.contents


prices = {}

for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string
    # print(f'{fixed_name} : {fixed_price}')
    # Or
    prices[fixed_name] = fixed_price

# sending data to an output file
with open('coin_coverage.txt', 'w') as f:
    with redirect_stdout(f):
        print(f'Current DT: {dt_string}\n')
        pprint.pprint(prices)





# print(list(trs[0].descendants))