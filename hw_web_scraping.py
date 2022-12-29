import requests
from bs4 import BeautifulSoup

URL = 'https://habr.com/ru/all/'
base_url = 'https://habr.com'
KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'JavaScript']

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'

response = requests.get(URL, headers={"User-Agent": user_agent})
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
articles_list = soup.find('div', class_='tm-articles-list')
all_article_items = articles_list.findAll('article', class_='tm-articles-list__item')
with open('data.txt', 'wt', encoding='utf-8') as file:
    for article in all_article_items:
        date = article.find('time')
        title = article.find('h2', class_='tm-article-snippet__title')
        link = title.find('a', class_='tm-article-snippet__title-link')
        tags_element = article.find('div', class_='tm-article-snippet__hubs')
        tags = tags_element.findAll('span', class_='tm-article-snippet__hubs-item')
        tags = [tag.text.strip('* ') for tag in tags]
        text = article.find('div', class_='article-formatted-body').text
        for kw in KEYWORDS:
            if kw in title or kw in tags or kw in text:
                print(f'{date.text} - {title.text} - {base_url}{link.get("href")}')
                break




# import requests
# from bs4 import BeautifulSoup
# URL = 'https://habr.com/ru/hub/python/'
# base_url = 'https://habr.com'
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
# KEYWORDS = "микросервисами"
# response = requests.get(URL, headers={"User-Agent": user_agent})
# # print(response.text)
## soup = BeautifulSoup(response.text, 'html.parser')
# articles_list = soup.find('div', class_='tm-articles-list')
# all_article_items = articles_list.findAll('article', class_='tm-articles-list__item')
# print(all_article_items)

# with open('data.txt', 'wt', encoding='utf-8') as file:
#     if KEWWORDS in articles_list:
#         print('XXX')
        # for article in all_article_items:
        #     date = article.find('time')
        #     title = article.find('h2', class_='tm-article-snippet__title')
        #     link = title.find('a', class_='tm-article-snippet__title-link')
        #     print(f'{date.text} - {title.text} - {base_url}{link.get("href")}')
        #     item = {'date': date.text, "title": title.text, "link": f'{base_url}{link.get("href")}'}
        #     file.write(f'{date.text} - {title.text} - {base_url}{link.get("href")}\n')
#
# with open('data.txt', 'wt', encoding='utf-8') as file:
#     for article in all_article_items:
#         date = article.find('time')
#         title = article.find('h2', class_='tm-article-snippet__title')
#         link = title.find('a', class_='tm-article-snippet__title-link')
#         print(f'{date.text} - {title.text} - {base_url}{link.get("href")}')
#         item = {'date': date.text, "title": title.text, "link": f'{base_url}{link.get("href")}'}
#         file.write(f'{date.text} - {title.text} - {base_url}{link.get("href")}\n')
