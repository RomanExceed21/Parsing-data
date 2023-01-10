from lxml import html
import requests

url = 'https://mail.ru/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Content-Type': 'text/html',
}
response = requests.get(url, headers=headers)
dom = html.fromstring(response.content)

link_list = dom.xpath('//a[@class="news-item-link svelte-19purc0"]')