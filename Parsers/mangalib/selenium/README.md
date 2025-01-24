# TikTok Video Downloader

Этот скрипт позволяет парсить последние обновления манги с сайта Mangalib обращаясь к неофициальному api, для парсинга используем selenium

## Установка

1. Убедитесь, что у вас установлен Python 3.8 или выше.
2. Клонируйте репозиторий (если вы используете Git):
   ```bash
   git clone https://github.com/MrTimofeev/Parsers.git
   cd mangalib/selenium
   ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Убедитесь, что у вас установлен `chromedriver`. Укажите путь к нему в файле `config.json`.

## Использование

1. Откройте файл `config.json` и настройте параметры:
   - `driver_path`: Укажите путь к `chromedriver`.
   - `user_agent`: Укажите User-Agent, если нужно.
   - `headless`: Настрока Selenium для видимости работы браузера при парсинге.
   - `page_number`: Номер страницы которую нужно спарсить (1 старница это самые новые обновления)


2. Запустите скрипт:
   ```bash
   python paeser_mangalib_api.py
   ```

4. Результаты будут сохранены в файл `manga_page_1.json`.


## Лицензия

Этот проект распространяется под лицензией [MIT](../../../LICENSE.txt)
