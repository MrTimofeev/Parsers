from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import undetected_chromedriver as uc

url = "https://www.ozon.ru/?__rr=1&abt_att=1&origin_referer=duckduckgo.com"



try:
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36')
    driver = uc.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    driver.get(url=url)
    time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    print("close parser")
    driver.close()
    driver.quit()
