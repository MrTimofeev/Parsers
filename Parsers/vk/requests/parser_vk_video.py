import requests
from bs4 import BeautifulSoup
import re

headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}


url = ""

first_respons = requests.get(url=url, headers=headers)
soup = BeautifulSoup(first_respons.text, 'lxml')
first_url_video = soup.find("meta", {"property": "og:video"})["content"]

second_respons = requests.get(url=first_url_video, headers=headers)
soup2 = BeautifulSoup(second_respons.text, 'lxml')
secons_url_video = str(soup2.findAll("script")[-1])

result_url = re.search(r"url720.*dash_sep", secons_url_video).group()
# print(result_url)

# Регулярное выражение для поиска ссылок
url_pattern = r'https:\\/\\/[^",]+'

# Поиск всех ссылок в строке
urls = re.findall(url_pattern, result_url)

# Замена обратных слэшей на обычные
cleaned_urls = [url.replace('\\/', '/') for url in urls]
print(cleaned_urls[0])

third_response = requests.get(url=cleaned_urls[0], headers=headers)

with open("test.mp4", "wb") as file:
        file.write(third_response.content)