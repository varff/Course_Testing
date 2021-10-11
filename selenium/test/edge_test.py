from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Edge('D:\\edge\\msedgedriver.exe')
driver.get('https://edufpmi.bsu.by/login/index.php')

login = driver.find_element_by_id('username')
login.send_keys('fpm.varfolom')

password = driver.find_element_by_id('password')
print('Enter password')
password.send_keys(input())
password.submit()

my = driver.get('https://edufpmi.bsu.by/my')

pe_att = driver.get('https://edufpmi.bsu.by/mod/attendance/view.php?id=21157')

while True:
    try:
        elem = driver.find_element_by_id('next-activity-link')
        elem.click()
    except NoSuchElementException:
        break

print(driver.title)
driver.quit()