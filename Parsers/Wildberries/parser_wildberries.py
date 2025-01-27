from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
import pprint
import json
import csv
import re


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
    executable_path="D:\\python progect\\Posting_vk_bot\\folder\\chromedriver.exe")
url = "https://www.wildberries.ru/catalog/0/search.aspx?search=%D0%BD%D0%B0%D1%83%D1%88%D0%BD%D0%B8%D0%BA%D0%B8"
driver = webdriver.Chrome(service=s, options=options)

result = []
count_item = 1
pattern = r"\d+"
try:
    for i in range(1, 10):
        driver.get(
            url=f"https://www.wildberries.ru/catalog/0/search.aspx?page={i}&sort=popular&search=%D0%BD%D0%B0%D1%83%D1%88%D0%BD%D0%B8%D0%BA%D0%B8")
        time.sleep(2)

        last_height = driver.execute_script(
            "return document.body.scrollHeight")
        while True:
            # Прокрутка вниз
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            # Пауза, пока загрузится страница.
            time.sleep(2)
            # Вычисляем новую высоту прокрутки и сравниваем с последней высотой прокрутки.
            new_height = driver.execute_script(
                "return document.body.scrollHeight")
            if new_height == last_height:
                print("Прокрутка завершена")
                break

            last_height = new_height
            # print("Появился новый контент, прокручиваем дальше")

        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'lxml')

        all_items = soup.findAll(
            "div", attrs={'class': 'product-card__wrapper'})

        try:
            for i in all_items:
                link_and_name = i.find(
                    "a", attrs={'class': 'product-card__link j-card-link j-open-full-product-card'})

                price_new = i.find(
                    "ins", attrs={'class': 'price__lower-price wallet-price red-price'})

                price_old = i.find("del")

                grade = i.find(
                    "span", attrs={'class': 'address-rate-mini address-rate-mini--sm'})

                count_grade = i.find(
                    "span", attrs={'class': 'product-card__count'})

                data = {}
                data["id"] = count_item
                data['name'] = link_and_name["aria-label"]
                data['link'] = link_and_name["href"]
                data['current_price'] = None if price_new == None else int(
                    "".join(re.findall(pattern, price_new.text)))
                data['old_price'] = int(
                    "".join(re.findall(pattern, price_old.text)))
                data['grade'] = "".join(re.findall(pattern, grade.text))
                data['count_grade'] = int(
                    "".join(re.findall(pattern, count_grade.text)))

                result.append(data)
                count_item += 1

        except Exception as ex:
            print(f"Что-то пошло не так: {ex}")

    # Открываем файл в режиме записи
    with open("data_result_parse_wb\\data.json", "w") as file:
        json.dump(result, file)

    with open('data_result_parse_wb\\data.csv', mode='w', newline='') as file:
        fieldnames = ['id', 'name', 'link', 'current_price',
                      'old_price', 'grade', 'count_grade']
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        # Write data to csv file
        for item in result:
            writer.writerow(item)
            print(item)

    pprint.pprint(result)


except Exception as ex:
    print(ex)
finally:
    print("close parser")
    driver.close()
    driver.quit()
