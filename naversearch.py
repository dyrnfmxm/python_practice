import requests
from selenium import webdriver
from bs4 import BeautifulSoup


driver = webdriver.Chrome('/Users/user/Downloads/chromedriver')
driver.implicitly_wait(3) 
driver.get('https://www.naver.com/') 
driver.find_element_by_name('query').send_keys('L’As du Fallafel')
driver.find_element_by_id("search_btn").click()
driver.find_element_by_xpath('//*[@id="lnb"]/div/div[1]/ul/li[2]').click()


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
 
title_list = soup.select('#elThumbnailResultArea > li.sh_blog_top > dl > dt')
for idx, title in enumerate(title_list, 1):
    print(title.text)
