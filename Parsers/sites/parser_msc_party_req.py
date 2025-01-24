import requests
import csv
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
}


for i in range(37):
    url = f"https://kudago.com/msk/events/?get_facets=1&page={i}"
    response = requests.get(
        url=url,
        headers=headers,
    )

    soup = BeautifulSoup(response.content, 'lxml')
    all_data = soup.find_all("article", attrs={'class': 'post post-rect'})
    # print(all_data)
    for i in all_data:
        result_dict = {}
        result_dict["Название"] = i.find("h2").find("span").text
        try:
            result_dict["Дата"] = i.find("time").find_all("div")[1].text
        except:
            result_dict["Дата"] = "Не указанно"
        # print(i.find("time").find_all("div")[1].text)

        try:
            if len(i.find_all("span")) == 9 and "все даты" not in i.find_all("span")[-3].text:
                result_dict["место"] = i.find_all("span")[-3].text
            else:
                result_dict["место"] = "Не указано"
        except:
            result_dict["место"] = "Не указано"
        
        with open('result_data.csv', 'a', newline="", encoding="Utf-8") as csvfile:
            fieldnames = ["Название", "Дата", "место"]

            writer = csv.DictWriter(
                csvfile, fieldnames=fieldnames, delimiter=";")
            writer.writerow(result_dict)
