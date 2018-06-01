# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ProblemItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    problem_no = Field()
    problem_name = Field()
    description = Field()
    input = Field()
    output = Field()
    sample_input = Field()
    sample_output = Field()
    hint = Field()
    source = Field()
    memory_limit = Field()
    time_limit = Field()

