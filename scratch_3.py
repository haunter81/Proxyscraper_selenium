from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.headless = True
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)

driver.get("https://hidemyna.me/en/proxy-list/")
time.sleep(10)


tbody = driver.find_element_by_tag_name("tbody")
cell = tbody.find_elements_by_tag_name("tr")

for column in cell:
    column = column.text.split(" ")
    print (column[0]+":"+ column[1])

driver.quit()