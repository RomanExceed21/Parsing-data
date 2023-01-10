import pprint
from pymongo import MongoClient
from lxml import html
from datetime import date
from pprint import pprint
import requests

client = MongoClient('mongodb://localhost:27017/')
python_db = client.python
collection = python_db.news
python_db.news.drop()

url = 'https://news.mail.ru/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Content-Type': 'text/html',
}
response = requests.get(url, headers=headers)
dom = html.fromstring(response.content)

link_list = dom.xpath('//span[@class="list__item__inner"]/a[@class="list__text"]')
all_main_news = []

for links_counter in range(len(link_list)):
    one_news_data = {}
    one_news_data["source_name"] = 'news.mail.ru'
    news_name = dom.xpath('//span[@class="list__item__inner"]/a[@class="list__text"]/text()')[links_counter]
    one_news_data["new's_name"] = ' '.join(news_name.split('\xa0'))
    one_news_data["new's_link"] = dom.xpath('//span[@class="list__item__inner"]/a[@class="list__text"]/@href')[links_counter]
    one_news_data["new's_date"] = str(date.today())
    all_main_news.append(one_news_data)

def insert_news_to_db(all_news_data):
    for one_news in all_news_data:
        collection.insert_one(one_news)

insert_news_to_db(all_main_news)

news_from_db = python_db.news.find()
for one_record in news_from_db:
	pprint(one_record)
