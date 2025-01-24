import time
import json
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import pprint

class MangalibParser:
    def __init__(self, config_path="config.json"):
        # Загрузка конфигурации из файла
        with open(config_path, "r", encoding="utf-8") as config_file:
            self.config = json.load(config_file)

        # Настройка опций Chrome
        self.chrome_options = uc.ChromeOptions()
        self.chrome_options.add_argument(f"user-agent={self.config['user_agent']}")
        if self.config.get("headless", False):
            self.chrome_options.add_argument("--headless")

        # Инициализация драйвера
        self.driver = uc.Chrome(options=self.chrome_options)
        self.driver.implicitly_wait(5)

    def parse_page(self):
        try:
            self.driver.get(url=self.config["url"])
            time.sleep(5)
            html_content = self.driver.page_source
            soup = BeautifulSoup(html_content, "lxml")

            result_dict = []
            all_content = soup.find_all("div", attrs={"class": "section paper"})
            all_content = all_content[0].find_all("div", attrs={"class": "xs_b8"})

            for i in all_content:
                # Блок с названием и ссылкой на всю мангу
                manga_href_and_name = i.find("div", attrs={"class": "xs_b1"})

                # Блок номером новой главы и ссылкой на эту главу
                all_manga_new_chapter = i.find("div", attrs={"class": "xs_g0"})

                # Словарь для записи в JSON
                _dict = {}

                # Получение названия и ссылки
                manga_name = manga_href_and_name.find("a", attrs={"class": "xs_ba"})
                _dict["Manga_name"] = " ".join(manga_name.text.split())
                _dict["link_manga"] = "https://mangalib.org" + manga_name["href"]

                # Получение новой главы и ссылки на новую главу
                manga_new_chapter = all_manga_new_chapter.find("a", attrs={"class": "xs_ba"})
                _dict["new_chapter"] = manga_new_chapter.text
                _dict["new_chapter_link"] = "https://mangalib.org" + manga_new_chapter["href"]

                # Записываем данные в результат
                result_dict.append(_dict)

            # Вывод результата в консоль
            pprint.pprint(result_dict)

            # Сохранение результата в JSON-файл
            with open(self.config["output_file"], "w", encoding="utf-8") as file:
                json.dump(result_dict, file, ensure_ascii=False)

        except Exception as ex:
            print(f"Ошибка: {ex}")
        finally:
            self.close()

    def close(self):
        print("Закрытие парсера")
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    parser = MangalibParser()
    parser.parse_page()