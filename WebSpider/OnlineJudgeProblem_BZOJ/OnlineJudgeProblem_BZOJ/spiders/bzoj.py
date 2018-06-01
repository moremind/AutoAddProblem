# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request, Spider
from urllib import parse
import re
from bs4 import BeautifulSoup
from lxml import etree
from OnlineJudgeProblem_BZOJ.items import ProblemItem


class BzojSpider(scrapy.Spider):
    name = 'bzoj'
    allowed_domains = []
    start_urls = 'http://172.16.72.4:83/'
    url = 'http://172.16.72.4:83/'

    def start_requests(self):
        yield Request(self.start_urls, callback=self.parse, dont_filter=False)

    def parse(self, response):
        """
        :function: 解析所有题目的url
        :param response: response
        :return:
        """

        # 解析所有题目url
        problem_urls = response.xpath('//table[@class="ui celled table"]/tbody//tr//td//a//@href').extract()

        for problem_url in problem_urls:

            detail_url = parse.urljoin(self.url, problem_url)

            yield Request(detail_url, self.parse_problem, dont_filter=False)

        # detail_url = 'http://172.16.72.4:83/JudgeOnline/1169.html'
        # yield Request(detail_url, self.parse_problem, dont_filter=False)

    def parse_problem(self, response):
        """
        :function:解析
        :param response:
        :return:
        """
        # 题号与题目数据
        problem = response.xpath('//div[@class="ui existing segment"]/center/h1//text()').extract_first()
        problem = str(problem)
        problem_no = re.sub("\D+", "", problem)[0:4]
        problem_names = re.findall(r": (.*)", problem, re.S)
        problem_name = problem_names[0]

        # 题目具体数据处理
        contents = response.xpath('.//div[@class="content"]')
        description = ''.join(contents[0].xpath(".").extract()).strip()
        input = ''.join(contents[1].xpath(".").extract()).strip()
        output = ''.join(contents[2].xpath(".").extract()).strip()
        sample_input = ''.join(contents[3].xpath(".//text()").extract()).strip()
        sample_output = ''.join(contents[4].xpath(".//text()").extract()).strip()
        hint = ''.join(contents[5].xpath(".").extract()).strip()
        source = ''.join(contents[6].xpath(".//text()").extract()).strip()

        if(hint == ""):
            hint = "没有提示"
        if(source == ""):
            source = "bzoj数据"

        memory_limit = 512
        time_limit = 1500

        problem_item = ProblemItem()
        for field in problem_item.fields:
            try:
                problem_item[field] = eval(field)
            except NameError:
                self.logger.debug('Field is Not Defined' + field)

        yield problem_item
