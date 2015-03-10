from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
browser.get('https://www.google.com.au')
searchbox = browser.find_element_by_name('q')
searchbox.send_keys('microsoft virtual academy python')
browser.find_element_by_name('btnG').click()
sleep(5)
browser.get('http://www.microsoftvirtualacademy.com/training-courses/introduction-to-programming-with-python')
#browser.close()