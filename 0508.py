from bs4 import BeautifulSoup
from selenium import webdriver


driver = webdriver.Chrome('/Users/user/Downloads/chromedriver')


driver.get('https://www.powderroom.co.kr/rankings/c1100')


bs = BeautifulSoup(driver.page_source, 'lxml')
titles = bs.findAll('div', attrs = {'class':'fs-5 tc-gray-1'})
ti = 0
for title in titles:
    result = str(title.find_all(text=True))
    print(result)
driver.quit()
