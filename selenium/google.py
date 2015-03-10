from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
browser.get('https://www.google.com.au')
searchbox = browser.find_element_by_name('q')
searchbox.send_keys('microcontroller melbourne moorabbin')
browser.find_element_by_name('btnG').click()
sleep(20)
browser.close()