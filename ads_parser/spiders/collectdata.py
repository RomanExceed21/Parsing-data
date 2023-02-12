import scrapy
from scrapy.http import HtmlResponse


class CollectdataSpider(scrapy.Spider):
    name = 'collectdata'
    allowed_domains = ['castorama.ru']
    start_urls = ['https://www.castorama.ru/']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [
            f'https://www.castorama.ru/{kwargs.get("search")}/']

    def parse(self, response):
        print()
        # links = response.xpath("//div[@data-cy='l-card']/a")
        # for link in links:
        #     yield response.follow(link, callback=self.parse_ads)

    # def parse_ads(self, response: HtmlResponse):
    #     loader = ItemLoader(item=AdsParserItem(), response=response)
    #     loader.add_xpath('name', "//h1/text()")
    #     loader.add_xpath('price', "//h3//text()")
    #     loader.add_xpath(
    #         'photos', "//div[@class='swiper-zoom-container']/img/@src | //div[@class='swiper-zoom-container']/img/@data-src")
    #     loader.add_value('url', response.url)
    #     yield loader.load_item()

    # name = response.xpath("//h1/text()").get()
        # price = response.xpath("//h3//text()").getall()
        # photos = response.xpath("//div[@class='swiper-zoom-container']/img/@src | //div[@class='swiper-zoom-container']/img/@data-src").getall()
        # url = response.url
        # yield AdsParserItem(name=name, price=price, photos=photos, url=url)
