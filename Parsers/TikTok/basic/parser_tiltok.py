# main.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import json

# Загрузка конфигурации из JSON-файла
with open("config.json", "r", encoding="utf-8") as config_file:
    config = json.load(config_file)

def download_video(url):
    """
    Скачивает видео с TikTok по указанной ссылке.

    :param url: Ссылка на видео TikTok.
    """
    # Настройки Selenium
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={config['user_agent']}")
    if config["selenium_options"]["headless"]:
        options.add_argument("--headless")

    # Инициализация драйвера
    service = Service(executable_path=config["chromedriver_path"])
    driver = webdriver.Chrome(service=service, options=options)

    try:
        print("Запуск Selenium...")
        driver.get(url)

        # Ждём, пока видео станет доступным
        WebDriverWait(driver, config["download_settings"]["timeout"]).until(
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
            with open(config["download_settings"]["output_path"], "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print(f"Видео успешно скачано и сохранено как {config['download_settings']['output_path']}!")
        else:
            print(f"Ошибка при загрузке видео: {response.status_code}")

    except Exception as ex:
        print(f"Ошибка: {ex}")
    finally:
        print("Закрытие Selenium.")
        driver.quit()

if __name__ == "__main__":
    # Укажите ссылку на видео TikTok
    url = ""  # Замените на реальную ссылку
    download_video(url)