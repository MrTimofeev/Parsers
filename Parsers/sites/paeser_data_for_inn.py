import requests
import csv
from bs4 import BeautifulSoup


with open('Data.csv', newline='', encoding="Windows-1251") as File:
    reader = csv.reader(File)
    for row in reader:
        try:
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
            }

            response = requests.get(
                f'https://zachestnyibiznes.ru/search?query={row}',
                headers=headers,
            )

            print(response.status_code)
            soup = BeautifulSoup(response.content, 'lxml')
            all_data = soup.find_all(
                "div", attrs={'class': 'background-grey-blue-light p-15 b-radius-5 m-b-20'})
            if len(all_data) == 0:
                print("Данных не найдено")
                continue
            else:
                print(f"Найдено {len(all_data)} данных")

            for i in all_data:
                result = {}
                result["Название фирмы"] = i.find("p", attrs={
                                                  'class': "no-indent m-b-5 f-s-16 c-black"}).find("a").text.replace("\t", "").replace("\n", "")
                result["Ссылка"] = "https://zachestnyibiznes.ru" + i.find(
                    "p", attrs={'class': "no-indent m-b-5 f-s-16 c-black"}).find("a")["href"]
                result["Статус"] = i.find_all("p", attrs={
                                              'class': 'no-indent m-b-5 c-black'})[0].text.replace("\t", "").replace("\n", "")
                result["ИНН"] = i.find_all("p", attrs={'class': 'no-indent m-b-5 c-black'})[
                    3].find_all("span")[1].text.replace("\t", "").replace("\n", "")
                result["ОГРНИП"] = i.find_all("p", attrs={'class': 'no-indent m-b-5 c-black'})[
                    3].find_all("span")[3].text.replace("\t", "").replace("\n", "")

                result["Деятельность"] = i.find("div", attrs={
                                                'class': 'no-indent m-b-5 c-black position-rel b-radius-5 p-5'}).text.replace("\t", "").replace("\n", "")
                with open('result_data.csv', 'a', newline="", encoding="Windows-1251") as csvfile:
                    fieldnames = ["Название фирмы", "Ссылка",
                                  "Статус", "ИНН", "ОГРНИП", "Деятельность"]

                    writer = csv.DictWriter(
                        csvfile, fieldnames=fieldnames, delimiter=";")
                    writer.writerow(result)
        except Exception as ex:
            print(f"Что-то пошло не так с этим ИНН: {row}, ошибка:{ex}")
