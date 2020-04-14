#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
from lxml.html import fromstring
from requests import get
from bs4 import BeautifulSoup


URL = 'https://www.marathonbet.com/su/popular/Football'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) Chrome/80.0.3987.163'
HEADERS = {'user-agent': USER_AGENT, 'accept' : '*/*'}
games = '//table[@class="coupon-row-item"]'
page = get(URL, headers=HEADERS)

if page.status_code.__eq__(200):
  html = fromstring(page.text)
  events = [event.text_content().replace('\n', '') for event in html.xpath(games)]
  print(events)
else:
  print('Error')
