import time
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import csv


try:
    
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36')
    driver = uc.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    for i in range(37):
        url = f"https://kudago.com/msk/events/?get_facets=1&page={i}"
        driver.get(url=url)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        all_data = soup.find_all("article", attrs={'class': 'post post-rect'})
        for i in all_data:
            result_dict = {}
            print()
            result_dict["Название"] = i.find("h2", attr={"class":"post-title"}).find("span").text,
            result_dict["Дата"] = i.find_all("div", attr={"class": "date-item"})[-1].text

            try:
                result_dict["место"] = i.find("span", attr={"class": "post-detail--event-place"}).text
            except:
                result_dict["место"] = "Не указано"

            with open('result_data.csv', 'a', newline="", encoding="Windows-1251") as csvfile:
                    fieldnames = ["Название", "Дата","место"]

                    writer = csv.DictWriter(
                        csvfile, fieldnames=fieldnames, delimiter=";")
                    writer.writerow(result_dict)   
        time.sleep(2)

except Exception as ex:
    print(ex)
finally:
    print("close parser")
    driver.close()
    driver.quit()
