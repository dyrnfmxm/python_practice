from selenium import webdriver

driver = webdriver.Chrome('/Users/user/Downloads/chromedriver')
driver.implicitly_wait(3) 
driver.get('https://www.google.co.kr/maps') 
driver.find_element_by_name('q').send_keys('L’As du Fallafel') 
driver.find_element_by_id("searchbox-searchbutton").click()


elem = driver.find_element_by_xpath('//*[@id="pane"]/div/div[2]').text
print(elem)
