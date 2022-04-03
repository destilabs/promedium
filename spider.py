import os
import pandas as pd
import numpy as np

from tools.setups import get_local_safe_setup
from tools.helpers import get_element_by_selector

from bs4 import BeautifulSoup
import argparse

import time

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--url', type=str, help='URL to scrape')
    parser.add_argument('--page_count', type=int, default=1, help='Number of pages to scrape [Number of posts saved divided by 20]')
    parser.add_argument('--output', type=str, default='./outputs/output.csv', help='Output file')

    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.output), exist_ok=True)

    driver = get_local_safe_setup()

    try:
        driver.get(args.url)
    except:
        print(f'Error loading {args.url}. Make sure you have made your reading list public.')
        driver.quit()

    for i in range(1, args.page_count + 1):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print(f"Scroll #{i}")
        time.sleep(5)

    src = BeautifulSoup(driver.page_source, 'lxml')

    selectors = ['h2', 'p', '.lg', '.lp']

    hackathon_content = np.array([
        [get_element_by_selector(div, selector) for selector in selectors]
            for div in src.select('article')])

    df = pd.DataFrame(hackathon_content, columns = ['Title', 'Author', 'Description', 'Tags'])

    df.to_csv(args.output, index=False)

    driver.quit()