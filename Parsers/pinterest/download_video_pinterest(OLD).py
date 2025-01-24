from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import requests
import re

options = webdriver.ChromeOptions()

# user-agent
options.add_argument(
    'user-agent=Mozilla/5.0 ("Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36')

# Run in the background
options.add_argument("--headless")

s = Service(
    executable_path="D:\\python progect\\test_parse\\folder\\chromedriver.exe")


url = "https://ru.pinterest.com/pin/127789708170905294/"

driver = webdriver.Chrome(service=s, options=options)


try:
    driver.get(url=url)
    time.sleep(3)
    responce = requests.get(url)
    text_html_syte = str(responce.content)

    url = re.search(r"https://v1.pinimg.com/videos.*.mp4",
                    text_html_syte).group()

    url = url.split("\"")
    for i in url:
        if ".mp4" in i and "https://v1.pinimg.com/videos" in i and "720p" in i:
            url = i
            break
    print(url)

    response = requests.get(url)

    with open("video.mp4", "wb") as file:
        file.write(response.content)

    time.sleep(5)


except Exception as ex:
    print(ex)
finally:
    print("close parser")
    driver.close()
