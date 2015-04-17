# -*- coding: utf-8 -*-

from scrapy import Item, Field


class DbSpiderItem(Item):
    book_name = Field()
    book_star = Field()
    book_rating = Field()
    book_eval = Field()
    book_author = Field()
    book_publish = Field()
    book_publish_date = Field()
    book_price = Field()