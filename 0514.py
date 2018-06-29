from selenium import webdriver
from bs4 import BeautifulSoup


driver = webdriver.Chrome('/Users/user/Downloads/chromedriver')
driver.implicitly_wait(3)
driver.get('https://www.google.co.kr/search?ei=8D_5WqDHGIH38QWPlbTQAg&q=l%27as+du+fallafel&oq=l%27as+du+fallafel&gs_l=psy-ab.3...0.0.0.225147.0.0.0.0.0.0.0.0..0.0....0...1..64.psy-ab..0.0.0....0.NOg4JBie9o0')
#driver.find_element_by_name('q').send_keys('L’As du Fallafel') 
#driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[3]/center/input[1]').click()
driver.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[3]/a').click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser') 
elem = soup.select('#rhs_block > div > div.kp-blk.knowledge-panel.Wnoohf.OJXvsb > div > div.ifM9O > div:nth-child(2) > div.kp-header > div > div.fYOrjf.kp-hc > div.NFQFxe.viOShc.LKPcQc.mod > div > div.d1rFIf > div > span.kno-tr-ctx')
print(elem)

