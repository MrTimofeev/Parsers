# TikTok Video Downloader

Этот скрипт позволяет парсить последние обновления манги с сайта Mangalib, для парсинга используем undetected_chromedriver

## Установка

1. Убедитесь, что у вас установлен Python 3.8 или выше.
2. Клонируйте репозиторий (если вы используете Git):
   ```bash
   git clone https://github.com/MrTimofeev/Parsers.git
   cd mangalib/undetected_chromedriver
   ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Убедитесь, что у вас установлен `chromedriver`. Укажите путь к нему в файле `config.json`.

## Использование

1. Откройте файл `config.json` и настройте параметры:
   - `user_agent`: Укажите User-Agent, если нужно.
   - `url`: Адрес по которому будет происходить парсинг (лучше не менять, для удобства я просто вынес в конфиг)
   - `output_file`: Путь куда будет сохранены данные


2. Запустите скрипт:
   ```bash
   python parser_mangalib.py
   ```

4. Результаты будут сохранены в файл `manga.json`.


## Лицензия

Этот проект распространяется под лицензией [MIT](../../../LICENSE.txt)
