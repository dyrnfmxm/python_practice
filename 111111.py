import requests
from selenium import webdriver
from bs4 import BeautifulSoup


driver = webdriver.Chrome('/Users/user/Downloads/chromedriver')
driver.implicitly_wait(3) 
driver.get('http://m.airkorea.or.kr/sub_new/sub11.jsp') 


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
 
title_list = soup.select('#ttr2')
for idx, title in enumerate(title_list, 1):
    print(title.text)
