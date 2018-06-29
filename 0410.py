import requests
from bs4 import BeautifulSoup

url = 'https://www.yelp.com/search?find_loc=London,+United+Kingdom&start=0&sortby=review_count&cflt=restaurants'
for page in range (1,10):
    params = {
        'start': (page-1)*30,
        }

    response = requests.get(url, params=params)
    
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
 
    title_list = soup.select('h3.search-result-title > span[class*=indexed-biz-name] > a[class*=biz-name]')
 
    for idx, title in enumerate(title_list, 1):
        print(title.text)
