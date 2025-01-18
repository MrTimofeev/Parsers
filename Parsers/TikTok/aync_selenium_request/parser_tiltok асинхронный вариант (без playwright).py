import asyncio
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import json
import os

# Загрузка конфигурации из JSON-файла
def load_config():
    config_path = os.path.abspath("config.json")
    try:
        with open(config_path, "r", encoding="utf-8") as config_file:
            config = json.load(config_file)
        print("Конфигурация успешно загружена.")
        return config
    except FileNotFoundError:
        print(f"Ошибка: Файл {config_path} не найден.")
        exit(1)
    except json.JSONDecodeError:
        print("Ошибка: Некорректный формат JSON в config.json.")
        exit(1)

# Загрузка конфигурации
config = load_config()

# Функция для загрузки видео
def download_video(url):
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
            return None

        print(f"Видео URL: {video_url}")

        # Получаем cookies для запроса
        cookies = driver.get_cookies()
        session = requests.Session()
        for cookie in cookies:
            session.cookies.set(cookie["name"], cookie["value"])

        # Скачиваем видео
        response = session.get(video_url, stream=True)
        if response.status_code == 200:
            filename = config["download_settings"]["output_path"]
            with open(filename, "wb") as file:
                file.write(response.content)
            print(f"Видео сохранено как {filename}.")
            return filename
        else:
            print(f"Ошибка при загрузке видео: {response.status_code}")
            return None
    except Exception as ex:
        print(f"Ошибка: {ex}")
        return None
    finally:
        print("Закрытие Selenium.")
        driver.quit()

# Асинхронная обёртка
async def async_download_video(url):
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        return await loop.run_in_executor(pool, download_video, url)

# Пример использования с asyncio
async def main():
    url = ""
    filename = await async_download_video(url)
    if filename:
        print(f"Видео скачано: {filename}")

# Запуск
if __name__ == "__main__":
    asyncio.run(main())