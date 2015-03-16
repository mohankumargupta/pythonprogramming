from selenium import webdriver
from time import sleep
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By

delay = 5

browser = webdriver.Firefox()
browser.get('https://www.python.org')
sleep(delay)
browser.get('https://www.python.org/doc/')
sleep(delay)
browser.get('https://docs.python.org/3/')
sleep(delay)
browser.get('https://docs.python.org/3/tutorial/index.html')

for i in range(100,900, 100):
    sleep(delay/15)
    scrollHeight = "window.scroll(0,{})".format(i)
    browser.execute_script(scrollHeight)


#Python Language Reference (Documentation)
#what consitutes a valid python program 
# keywords, syntax
'''
browser.get('https://docs.python.org/3/reference/index.html')
for i in range(100,1500, 100):
    sleep(delay/5)
    scrollHeight = "window.scroll(0,{})".format(i)
    browser.execute_script(scrollHeight)
'''
#Python Library Reference (Documentation)
'''
browser.get('https://docs.python.org/3/reference/index.html')
'''

#browser.close()