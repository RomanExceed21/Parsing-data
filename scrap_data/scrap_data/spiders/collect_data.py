import scrapy
from scrapy.http import HtmlResponse
from scrap_data.items import ScrapDataItem


class CollectDataSpider(scrapy.Spider):
    name = 'collect_data'
    allowed_domains = ['citilink.ru']
    start_urls = ['https://www.citilink.ru']

    def parse(self, response: HtmlResponse):
        hits_products = response.xpath(
            '//div[@class="block_data__gtm-js block_data__pageevents-js between-card-banners_gtm-js between-card-banners_pageevents-js "]//div[@class="ProductCardVertical__description "]/a/@href').getall()
        for link in hits_products:
            link = 'https://www.citilink.ru'+link
            yield response.follow(link, callback=self.parse_products)
    
    def parse_products(self, response: HtmlResponse):
        product_name = response.css('h1::text').get().strip()
        product_sale = response.xpath(
            '//span[@class="ProductPrice__price ProductPagePriceSection__default-price__price"]/span[1]//text()').get().strip()
        product_unit = response.xpath(
            '//span[@class="ProductPrice__price ProductPagePriceSection__default-price__price"]/span[2]//text()').get().strip()
        yield ScrapDataItem(
            product=product_name,
            sale=product_sale,
            unit=product_unit,
        )
