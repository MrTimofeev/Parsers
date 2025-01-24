from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time



options = webdriver.ChromeOptions()

# user-agent
options.add_argument(
    'user-agent=Mozilla/5.0 ("Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36')


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}


# Run in the background
# options.add_argument("--headless")

s = Service(
    executable_path="D:\\python progect\\chromedriver\\chromedriver.exe")
url = "https://market.yandex.ru/search?text=kawaii"
driver = webdriver.Chrome(service=s, options=options)

try:
    driver.get(url=url)
    time.sleep(2)
    html_content = driver.page_source
    with open("test.html", "wb") as file:
        file.write(bytes(html_content, encoding="utf-8"))
    time.sleep(10)

#     with open("test.html", "r", encoding="utf-8") as file:
#         soup = BeautifulSoup(file.read(), 'lxml')

except Exception as ex:
    print(ex)
finally:
    print("close parser")
    driver.close()
    driver.quit()
