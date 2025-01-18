# TikTok Video Downloader (Playwright + Async)

Этот скрипт позволяет асинхронно скачивать видео с TikTok с использованием Playwright и aiohttp.

## Установка

1. Убедитесь, что у вас установлен Python 3.8 или выше.
2. Клонируйте репозиторий (если вы используете Git):
   ```bash
   git clone https://github.com/MrTimofeev/Parsers.git
   cd tiktok-video-downloader
   ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Установите браузеры для Playwright:
   ```bash
   playwright install
   ```

## Использование

1. Откройте файл `config.json` и настройте параметры:
   - `user_agent`: Укажите User-Agent, если нужно.
   - `tiktok_url`: Укажите ссылку на видео TikTok.
   - `download_settings`: Укажите путь для сохранения видео.
   - `playwright_settings`: Настройте браузер и режим headless.

2. Запустите скрипт:
   ```bash
   python main.py
   ```

3. Скачанное видео сохранится в файл, указанный в `download_settings["output_path"]`.

## Лицензия

Этот проект распространяется под лицензией [MIT](LICENSE).
```
