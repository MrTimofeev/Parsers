# Парсеры для социальных сетей

Этот репозиторий содержит набор парсеров для скачивания контента с различных социальных сетей и сайтов. Каждый парсер находится в отдельной папке и имеет свою документацию.

## Содержание

- [Установка](#установка)
- [Использование](#использование)
- [Список парсеров](#список-парсеров)
- [Лицензия](#лицензия)

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/MrTimofeev/Parsers.git
   cd parsers-repo
   ```

2. Установите зависимости для каждого парсера. Перейдите в папку с парсером и выполните:
   ```bash
   cd Parsers/TikTok/basic  # Пример для TikTok basic
   pip install -r requirements.txt
   ```

## Использование

Каждый парсер имеет свой собственный файл `README.md` с инструкциями по запуску. Перейдите в папку с нужным парсером и следуйте указаниям.

Пример запуска парсера:
```bash
python название_файла.py
```

## Список парсеров

Вот список доступных парсеров:

### TikTok
- **[parser_tiktok_v1](./Parsers/TikTok/basic/README.md)** — Синхронный парсер для скачивания видео с TikTok с использованием Selenium и reqests.
- **[parser_tiktok_v2](./Parsers/TikTok/aync_selenium_request/README.md)** — Асинхронный парсер для скачивания видео с TikTok с использованием Selenium и reqests.
- **[parser_tiktok_v3](./Parsers/TikTok/async_playwrigth_aiohttp/README.md)** — Асинхронный парсер для скачивания видео с TikTok с использованием Playwright и aiohttp.

## Важное предупреждение

Этот репозиторий и все содержащиеся в нём парсеры созданы **исключительно в ознакомительных и образовательных целях**. Автор не несёт ответственности за использование этих скриптов в нарушение правил платформ или законодательства.

Перед использованием парсеров убедитесь, что:
1. Вы имеете право на скачивание и использование контента.
2. Ваши действия не нарушают правила платформ (TikTok, Instagram, YouTube и других).
3. Вы не используете парсеры для незаконных или вредоносных целей.

Автор не поддерживает и не одобряет использование этих скриптов для:
- Нарушения авторских прав.
- Несанкционированного доступа к данным.
- Любых других действий, которые могут быть расценены как незаконные или неэтичные.

Используйте парсеры на свой страх и риск.

## Лицензия

Этот проект распространяется под лицензией [MIT](LICENSE.txt). Подробности см. в файле `LICENSE`.





