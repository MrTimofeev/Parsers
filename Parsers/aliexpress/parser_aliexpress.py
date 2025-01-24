import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import undetected_chromedriver as uc

url = "https://aliexpress.ru/wholesale?SearchText=%D0%BD%D0%B0%D1%83%D1%88%D0%BD%D0%B8%D0%BA%D0%B8+%D0%B1%D0%B5%D1%81%D0%BF%D1%80%D0%BE%D0%B2%D0%BE%D0%B4%D0%BD%D1%8B%D0%B5&g=y&page=1&searchInfo=A7DDfCCdkW6zdOQJjoZEUpZsFKmPnoiIHxdsBo9yVnQYwAfkGenEZ6vi5ZplNEaBKxKm6zMTaSLpvRufKLj9wdmwmYlUAhDq14yVdteG7Y10ji5aUjzGJGX%2FS2HsoSufejZX4QdHHBLuQIJ3ZDStyXKE9DJuvOMcBRnFOChLKdbb3RijuKb4yjma+JK11w7LgI0t69RzOd0zdYVJC3G989zFxiNAPwNIdM4atyxmBe7AXLExHdLTgtRzs4wdlB74q29mgkwWTALgmFE06hDNXn6hKLWivPqPXumLTXwYZnfQLsZgiIjHh4MCBp8cBPqp0dIIRSvgWFvkotlvrwa9F8zjcSmYreTkMc5kOUx7"



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


### временно не рабочий (не может пройти атибот систему)