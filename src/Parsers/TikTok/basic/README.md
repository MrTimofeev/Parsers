# TikTok Video Downloader

Этот скрипт позволяет скачивать видео с TikTok с использованием Selenium и Requests.

## Установка

1. Убедитесь, что у вас установлен Python 3.8 или выше.
2. Клонируйте репозиторий (если вы используете Git):
   ```bash
   git clone https://github.com/MrTimofeev/Parsers.git
   cd TikTok/basic
   ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Убедитесь, что у вас установлен `chromedriver`. Укажите путь к нему в файле `config.json`.

## Использование

1. Откройте файл `config.json` и настройте параметры:
   - `chromedriver_path`: Укажите путь к `chromedriver`.
   - `user_agent`: Укажите User-Agent, если нужно.
   - `selenium_options`: Настройте режим работы Selenium (например, headless).
   - `download_settings`: Укажите путь для сохранения видео и время ожидания.

2. Откройте файл `main.py` и укажите ссылку на видео TikTok:
   ```python
   url = ""  # Замените на реальную ссылку
   ```

3. Запустите скрипт:
   ```bash
   python main.py
   ```

4. Скачанное видео сохранится в файл, указанный в `download_settings["output_path"]`.


## Лицензия

Этот проект распространяется под лицензией [MIT](../../../../LICENSE.txt)
