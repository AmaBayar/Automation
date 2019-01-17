import time
from selenium import webdriver


driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get("https://www.youtube.com/")
time.sleep(0)
button = driver.find_element_by_xpath('//*[@id="buttons"]/ytd-button-renderer')
button.click()	
time.sleep(0)
email = driver.find_element_by_xpath('//*[@id="identifierId"]')
email.send_keys("Amabayar123@gmail.com")
Next_button = driver.find_element_by_xpath('//*[@id="identifierNext"]')
Next_button.click()
time.sleep(1)
password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password.send_keys("mongol55")
password_button = driver.find_element_by_xpath('//*[@id="passwordNext"]')
password_button.click()
time.sleep(1)
video = driver.find_element_by_xpath('//*[@id="video-title"]')
video.click()
time.sleep(2)
Sendmessage = driver.find_element_by_id('search').click()
Sendmessage.send_keys("Hello world")
# print(driver.title)s
driver.quit
