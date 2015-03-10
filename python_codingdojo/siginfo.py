from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
browser.get('http://stg.mpcug.net.au/early-public-release/list-of-recurrent-meetings-contact-details/')
sig_elements = browser.find_elements_by_xpath('//pre/strong[contains(text(), "SIG--subgroup")]')
number_of_sigs = 0
for e in sig_elements:
	print(e.text.replace('SIG--subgroup   ',''))
	number_of_sigs = number_of_sigs + 1
print('The number of SIGs at melbpc: ', number_of_sigs)
browser.close()
