from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import csv


options = webdriver.ChromeOptions()

# user-agent
options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36')

# Run in the background
options.add_argument("--headless")

s = Service(
    executable_path="D:\\python progect\\chromedriver\\chromedriver.exe")
url = ""
driver = webdriver.Chrome(service=s, options=options)


try:
    driver.get(url=url)
    time.sleep(15)
    result_link = []

    last_height = driver.execute_script("return document.body.scrollHeight")
    for _ in range(20):
        last_height = driver.execute_script("return document.body.scrollHeight")
        
        # Прокрутка вниз
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Пауза, пока загрузится страница.
        time.sleep(0.4)
        
        # Вычисляем новую высоту прокрутки и сравниваем с последней высотой прокрутки.
        new_height = driver.execute_script("return document.body.scrollHeight")
        
        if new_height == last_height:
            print("Прокрутка завершена")
            break
        

    All_link = driver.find_elements(By.TAG_NAME, "a")
    with open('Link_video.csv', mode='a', newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for item in All_link:
            Link_video = item.get_attribute("href")
            if "/clip" in Link_video:
                writer.writerow([Link_video])
                print(item.get_attribute("href"))


except Exception as ex:
    print(ex)
finally:

    print("close parser")
    driver.close()
