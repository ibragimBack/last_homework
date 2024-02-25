import httpx
from parsel import Selector

MAIN_URL = "https://www.house.kg/snyat"
BASE_URL = "https://www.house.kg"

def get_html(url):
    response = httpx.get(url)
    return Selector(response.text)

def get_title(html):
    title = html.css('title::text').get()
    return title

def get_houses_links(html):
    houses = html.css('.profile-navigation a::attr(href)').getall()
    links = list(map(lambda x: BASE_URL + x, houses))
    return links

if __name__ == '__main__':
    html = get_html(MAIN_URL)
    title = get_title(html)
    # print(title)
    links = get_houses_links(html)
    # print(links)