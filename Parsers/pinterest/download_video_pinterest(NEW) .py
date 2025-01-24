import requests
import re


headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}


url = "https://ru.pinterest.com/pin/316307573845680786/"

test_respons = requests.get(url=url, headers=headers)
print(test_respons.status_code)

url = re.search(r"https://v1.pinimg.com/videos.*.mp4", str(test_respons.content)).group()
url = url.split("\"")
for i in url:
        if ".mp4" in i and "https://v1.pinimg.com/videos" in i and "720p" in i:
                url = i
                break
        # print(url)

response = requests.get(url)

with open("video.mp4", "wb") as file:
        file.write(response.content)