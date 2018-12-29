from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import time

x = 0
i = 0

#options.headless = True     #for headless
#options.add_argument('--disable-gpu') #for headless and os win
options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(options=options)
driver.get('https://hidemyna.me/en/proxy-list/')
time.sleep(20) #bypass cloudflare

def scrape():
  i = 0
  #scrape
  tbody = driver.find_element_by_tag_name("tbody")
  cell = tbody.find_elements_by_tag_name("tr")

  for column in cell:
      column = column.text.split(" ")
      proxy_list_sel = column[0]+":"+ column[1] #ip and port
      f = open('seleniumprox.txt', 'a')  # writing to a file , not the final output due to empty lines
      f.write(proxy_list_sel + '\n')
      #print(proxy_list_sel)
      i = i + 1  # for debug and statistical reasons

  print (i)

def next_page():
  #next page
  driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[@class='arrow__right']/a"))))
  driver.find_element_by_xpath("//li[@class='arrow__right']/a").click()
  print("Navigating to Next Page")

count = 0

while count < 50:
  scrape()
  next_page()
  time.sleep(20)
  count = count + 1
  print (count , " times")

#removing empty lines
with open('seleniumprox.txt') as infile, open('output_sel.txt', 'w') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line)  # non-empty line. Write it to output

#driver.quit()
