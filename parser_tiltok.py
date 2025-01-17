from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

# Настройки Selenium
options = webdriver.ChromeOptions()
options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
)
options.add_argument("--headless")  # Можно отключить, если хотите видеть браузер

# Укажите путь к chromedriver
s = Service(executable_path="D:\\python progect\\Posting_vk_bot\\folder\\chromedriver.exe")

def download_video(url):
    driver = webdriver.Chrome(service=s, options=options)
    try:
        print("Запуск Selenium...")
        driver.get(url)

        # Ждём, пока видео станет доступным
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "video"))
        )

        # Получаем ссылку на видео
        video_url = driver.find_element(By.TAG_NAME, "video").get_attribute("src")
        if not video_url:
            video_url = driver.find_element(By.TAG_NAME, "source").get_attribute("src")

        if not video_url:
            print("Видео URL не найдено.")
            return

        print(f"Видео URL: {video_url}")

        # Получаем cookies для запроса
        cookies = driver.get_cookies()
        session = requests.Session()
        for cookie in cookies:
            session.cookies.set(cookie["name"], cookie["value"])

        # Скачиваем видео
        response = session.get(video_url, stream=True)
        if response.status_code == 200:
            with open("video.mp4", "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print("Видео успешно скачано!")
        else:
            print(f"Ошибка при загрузке видео: {response.status_code}")

    except Exception as ex:
        print(f"Ошибка: {ex}")
    finally:
        print("Закрытие Selenium.")
        driver.quit()

# Запуск
url = "ссылка на видос тт" 
download_video(url)
