import time
from selenium import webdriver

driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get("https://discordapp.com/")
button = driver.find_element_by_xpath('//*[@id="app-mount"]/div/div/section/div[1]/div/div/div/form/button').click()