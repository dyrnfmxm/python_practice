import requests
from bs4 import BeautifulSoup
 
 
url = 'https://search.naver.com/search.naver'
for page in range(1, 1000):
    params = {
        'query': '플래닛코스터',
        'where': 'post',
        'start': (page-1)*10+1,
    }
 
    response = requests.get(url, params=params)
    html = response.text
 
    soup = BeautifulSoup(html, 'html.parser')
 
    title_list = soup.select('.sh_blog_title')
 
    for tag in title_list:
        print(tag.text)
