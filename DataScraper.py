from _ast import Raise
from bs4 import BeautifulSoup
import requests
import time
import sys


def main():
    bs = ['Saint Petersburg', 'Tampa', 'Trinity', 'Wesley Chapel', 'Zephyrhills', ]
    db = ['Ybor', 'New Port Richey', 'Holiday', 'Brandon', 'Clearwater', 'Odessa', ]
    listings = bs + db

    print('Choose City for Free Items.')
    print('Cities to choose from:')
    print(bs)
    print(db)

    while True:
        city = input('>')
        if city in list(listings):
            print(f'Searching for the city of: {city}....')
            time.sleep(2)
            break

        else:
            print("ERROR, Enter Correct City")
        break

    page = 1
    inventory = 0
    found_items = set()
    while page <= 2 and inventory <= 100:
        url = \
            (f'https://tampa.craigslist.org/search/zip?language=5&query='
             f'free&srchType=T#search=1~list\\~{page}~{inventory}')
        page = page + 1
        inventory = inventory + 1
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'lxml')
        postings = soup.find_all('li', class_='cl-static-search-result')

        for posting in postings:
            title = posting.find('div', class_='title').text
            website = posting.a.attrs['href']
            location = posting.find('div', class_='location').text.strip()
            item_info = (title, website, location)
            if city.lower() in location.lower() and item_info not in found_items:
                found_items.add(item_info)
                print(f'website: {website}')
                print(f'title: {title},')
                print(f' location: {location}')
                print('')

        if not found_items:
            print(f'No free items were found for {city}')
            break


def research():
    x = input('Would you like to search another Area? (Yes or No)')
    if x.lower() == 'yes':
        print("Rerunning Program")
        main()
    elif x.lower() == 'no':
        sys.exit()
    else:
        print("Invalid input. Please enter 'Yes' or 'No'.")
        research()


if __name__ == '__main__':
    while True:
        main()
        research()
        time_wait = 2
        print(f'Waiting {time_wait} seconds...')
        time.sleep(time_wait)
