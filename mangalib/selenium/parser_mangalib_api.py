import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class MangalibParser:
    def __init__(self, config_path="config.json"):
        # Загрузка конфигурации из файла
        with open(config_path, "r", encoding="utf-8") as config_file:
            self.config = json.load(config_file)

        # Настройка опций Chrome
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(f"user-agent={self.config['user_agent']}")
        if self.config.get("headless", True):
            self.options.add_argument("--headless")

        # Инициализация драйвера
        self.service = Service(executable_path=self.config["driver_path"])
        self.driver = webdriver.Chrome(service=self.service, options=self.options)

    def parse_page(self, page_number=None):
        if page_number is None:
            page_number = self.config.get("page_number", 1)

        self.driver.get(url=f"https://api.mangalib.me/api/latest-updates?page={page_number}")
        time.sleep(2)
        manga_data = []
        json_data = self.driver.find_element(By.TAG_NAME, 'pre')
        try:
            data = json.loads(json_data.text)
            for item in data["data"]:
                result = {
                    "Русское название:": item["rus_name"],
                    "Английское название:": item["eng_name"],
                    "Ссылка на фото:": item["cover"]["default"],
                    "Ссылка на фото (Маленькое):": item["cover"]["thumbnail"],
                    "Возрастное ограничение:": item["ageRestriction"]["label"],
                    "Тип:": item["type"]["label"],
                    "Статус:": item["status"]["label"],
                    "Глава:": item["metadata"]["latest_items"]["items"][0]["number"],
                    "Том:": item["metadata"]["latest_items"]["items"][0]["volume"],
                    "url:": f"https://mangalib.org/ru/manga/{item['slug_url']}"
                }
                self.driver.get(url=f"https://api.mangalib.me/api/manga/{item['slug_url']}?fields[]=summary")
                time.sleep(1)
                json_data = self.driver.find_element(By.TAG_NAME, 'pre')
                data = json.loads(json_data.text)
                result['Описание'] = data["data"]["summary"]
                manga_data.append(result)
        except json.JSONDecodeError:
            print("Ошибка: данные не в формате JSON")
            data = None

        if data:
            with open(f'manga_page_{page_number}.json', 'w', encoding='utf-8') as json_file:
                json.dump(manga_data, json_file, ensure_ascii=False, indent=4)

        print(f"[INFO] Страница {page_number} добавлена")

    def close(self):
        self.driver.close()

if __name__ == "__main__":
    parser = MangalibParser()
    try:
        parser.parse_page()
    except Exception as ex:
        print(ex)
    finally:
        parser.close()
        print("Парсер закрыт")