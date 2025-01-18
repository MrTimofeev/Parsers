import asyncio
import json
import os
from playwright.async_api import async_playwright
import aiohttp

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
async def download_video(video_url, cookies):
    headers = {
        "User-Agent": config["user_agent"],
        "Referer": "https://www.tiktok.com/",
    }
    cookie_header = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
    headers["Cookie"] = cookie_header

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(video_url) as response:
            if response.status == 200:
                with open(config["download_settings"]["output_path"], "wb") as file:
                    while True:
                        chunk = await response.content.read(8192)
                        if not chunk:
                            break
                        file.write(chunk)
                print(f"Видео успешно скачано и сохранено как {config['download_settings']['output_path']}!")
            else:
                print(f"Ошибка при загрузке видео: {response.status}")

async def main():
    async with async_playwright() as p:
        # Настройки браузера
        browser_type = getattr(p, config["playwright_settings"]["browser"])
        browser = await browser_type.launch(headless=config["playwright_settings"]["headless"])
        context = await browser.new_context(user_agent=config["user_agent"])
        page = await context.new_page()

        await page.set_extra_http_headers({
            "dnt": "1",
            "referer": "https://www.tiktok.com/",
            "sec-ch-ua": "'Not)A;Brand';v='99', 'Google Chrome';v='127', 'Chromium';v='127'",
            "user-agent": config["user_agent"],
        })

        await page.route("**/*", lambda route: route.abort() if route.request.resource_type in ["image", "stylesheet", "font"] else route.continue_())

        await page.goto(config["tiktok_url"])

        try:
            captcha_close_button = page.locator("#captcha_close_button")
            await captcha_close_button.click(timeout=10000)
            await asyncio.sleep(4)
        except Exception:
            print("Кнопка закрытия капчи не найдена или не нужна")

        video_url = None
        try:
            video_element = page.locator("video").first
            video_url = await video_element.get_attribute("src")
            if not video_url:
                raise Exception("Ссылка в теге <video> пуста")
        except Exception as e:
            print(f"Ошибка при поиске в теге <video>: {e}")
            try:
                video_element = page.locator("source").first
                video_url = await video_element.get_attribute("src")
                if not video_url:
                    raise Exception("Ссылка в теге <source> пуста")
            except Exception as e:
                print(f"Ошибка при поиске в теге <source>: {e}")

        if video_url:
            print(f"Ссылка на видео: {video_url}")
        else:
            print("Ссылка на видео не найдена в тегах <video> и <source>.")
            await browser.close()
            return

        cookies = await context.cookies()
        await download_video(video_url, cookies)

        await browser.close()

# Запуск асинхронной функции
if __name__ == "__main__":
    asyncio.run(main())