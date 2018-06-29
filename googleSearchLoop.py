from selenium import webdriver

driver = webdriver.Chrome('/Users/user/Downloads/chromedriver')
driver.implicitly_wait(3)
driver.get('https://www.google.co.kr')
driver.find_element_by_name('q').send_keys('L’As du Fallafel') 
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[3]/center/input[1]').submit()

elem = driver.find_element_by_xpath('//*[@id="rhs_block"]/div/div[1]/div/div[1]/div[2]/div[4]/div/div').text
print(elem)
