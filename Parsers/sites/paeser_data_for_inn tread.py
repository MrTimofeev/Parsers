import requests
import csv
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

# Лок для безопасной записи в файлы из потоков
lock = threading.Lock()

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
}

def fetch_data(row):
    try:
        response = requests.get(f'https://zachestnyibiznes.ru/search?query={row}', headers=HEADERS)
        # print(f"Status Code: {response.status_code} for {row}")

        if response.status_code != 200:
            raise Exception(f"HTTP Error {response.status_code}")

        soup = BeautifulSoup(response.content, 'lxml')
        all_data = soup.find_all("div", attrs={'class': 'background-grey-blue-light p-15 b-radius-5 m-b-20'})

        if not all_data:
            print(f"Данных не найдено для {row}")
            return  # Пропускаем без ошибки

        print(f"Найдено {len(all_data)} записей для {row}")

        results = []
        for i in all_data:
            result = {
                "Название фирмы": i.find("p", attrs={'class': "no-indent m-b-5 f-s-16 c-black"})
                                      .find("a").text.strip(),
                "Ссылка": "https://zachestnyibiznes.ru" + i.find("p", attrs={'class': "no-indent m-b-5 f-s-16 c-black"})
                                      .find("a")["href"],
                "Статус": i.find_all("p", attrs={'class': 'no-indent m-b-5 c-black'})[0]
                            .text.strip(),
                "ИНН": i.find_all("p", attrs={'class': 'no-indent m-b-5 c-black'})[3]
                            .find_all("span")[1].text.strip(),
                "ОГРНИП": i.find_all("p", attrs={'class': 'no-indent m-b-5 c-black'})[3]
                            .find_all("span")[3].text.strip(),
                "Деятельность": i.find("div", attrs={'class': 'no-indent m-b-5 c-black position-rel b-radius-5 p-5'})
                                  .text.replace("\t", "").replace("\n", ""),
            }
            results.append(result)

        # Запись успешных данных в файл
        with lock:
            with open('result_data.csv', 'a', newline="", encoding="Windows-1251") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=results[0].keys(), delimiter=";")
                for result in results:
                    writer.writerow(result)

    except Exception as ex:
        print(f"Ошибка с {row}: {ex}")
        # Запись неудачных строк для повторного запуска
        with lock:
            with open('failed.csv', 'a', newline="", encoding="Windows-1251") as failed_file:
                failed_writer = csv.writer(failed_file)
                failed_writer.writerow([row])

def main():
    # Загружаем все строки из исходного CSV
    with open('Data.csv', newline='', encoding="Windows-1251") as f:
        reader = csv.reader(f)
        rows = [row[0] for row in reader if row]

    print(f"Всего строк для обработки: {len(rows)}")

    # Используем ThreadPoolExecutor для многопоточности
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(fetch_data, row) for row in rows]

        for future in as_completed(futures):
            future.result()  # Обрабатываем завершённые задачи

if __name__ == "__main__":
    main()
