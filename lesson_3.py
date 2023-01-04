import json
from pprint import pprint
from bs4 import BeautifulSoup as bs
import requests
from time import sleep

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Content-Type': 'text/html',
}

all_vacancy_data = []
page_counter = 0

while True:
    sleep(2)
    print(page_counter)
    url = \
        f'https://hh.ru/search/vacancy?text=python&from=suggest_post&area=1&customDomain=1&page={page_counter}&hhtmFrom=vacancy_search_list'
    print(url)
    response = requests.get(url, headers=headers)
    soup = bs(response.text, 'html.parser')
    div_with_vacancy_data = soup.findAll('div', {'class': 'vacancy-serp-item-body'})

    for link in div_with_vacancy_data:
        one_vacancy_data = dict()

        one_vacancy_data['vacancy_link'] = link.find('a')['href']
        one_vacancy_data['vacancy_text'] = link.select_one("div[class=''] h3[class='bloko-header-section-3']").text
        one_vacancy_data['source_site'] = 'hh.ru'

        if link.select_one("div[class=''] span[class='bloko-header-section-3']"):
            salary_info = link.select_one("div[class=''] span[class='bloko-header-section-3']").text
            one_vacancy_data['salary'] = ' '.join(salary_info.split())
        else:
            one_vacancy_data['salary'] = 'ЗП НЕ УКАЗАНА'

        all_vacancy_data.append(one_vacancy_data)

    if soup('a', {'data-qa': 'pager-next'}):
        page_counter += 1
    else:
        break

with open("data.json", "w") as f:
    json.dump(all_vacancy_data, f)
with open("data.json", "r") as f:
    pprint(json.load(f))
