from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('D:\\chrm\\chromedriver.exe')
driver.get('https://google.com')

driver.find_element_by_name('q').send_keys('lichess')
driver.find_element_by_name('q').submit()
driver.find_element_by_partial_link_text('lichess').click()
driver.get('https://lichess.org/login?referrer=')

driver.find_element_by_id('form3-username').send_keys('test_sel')
driver.find_element_by_id('form3-password').send_keys('1212llll')
driver.find_element_by_xpath('//*[@id="main-wrap"]/main/form/div[1]/button').click()

driver.find_element_by_partial_link_text('group')
