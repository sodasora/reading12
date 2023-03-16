import requests
from bs4 import BeautifulSoup

url = "https://product.kyobobook.co.kr/detail/S000001296687"
data = requests.get(url)
soup = BeautifulSoup(data.text, "html.parser")

img_tag = soup.select_one("img[src^='https://contents.kyobobook.co.kr/sih/fit-in/']")
img_url = img_tag.get("src")
print(img_url)

title_tag = soup.select_one("#contents > div.prod_detail_header > div > div.prod_detail_title_wrap > div > div.prod_title_box.auto_overflow_wrap > div.auto_overflow_contents > div > h1 > span")
title_name = title_tag.text
print(title_name)

author_tag = soup.select_one("#contents > div.prod_detail_header > div > div.prod_detail_view_wrap > div.prod_detail_view_area > div:nth-child(1) > div > div.prod_author_box.auto_overflow_wrap > div.auto_overflow_contents > div > div > a:nth-child(1)")
author_name = author_tag.text
print(author_name)