# Sprint_5 — Автотесты для Stellar Burgers

Автоматизированные тесты для веб‑сервиса Stellar Burgers с использованием Selenium.

## Технологии

* Python 3.x
* Selenium WebDriver
* Google Chrome
* pytest

## Установка и запуск

1. Установите зависимости:
   ```bash
   pip install -r requirements.txt

    Скачайте ChromeDriver и поместите в PATH или укажите путь в коде.

    Запустите тесты:

        Все тесты: pytest tests/ -v

        Отдельные файлы: pytest tests/test_registration.py -v

Структура проекта

    urls.py — основные URL сервиса

    locators.py — локаторы элементов интерфейса

    helps.py — вспомогательные функции (генераторы email и паролей)

    conftest.py — фикстуры pytest

    tests/ — директория с тестами
