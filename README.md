# Куда пойти - Москва глазами Артёма
### Самые интересные места в Москве

[Cайт](http://morelinks.to) | [Административный раздел](http://morelinks.to/admin/)

## Usage

Проект предполагает использование PostGIS.

- Скопируйте файл переменных окружения из шаблона:
``` Bash
cp .env.template .env
```
- Заполните переменные окружения в файле `.env`

- Для запуска через Docker в директории проекта выполните команду

``` Bash
docker compose up -d --build
```

По умолчанию проект будет доступен по адресу http://localhost:8001

## Contribution

При запуске через Docker директория проекта подключается как [bind mount](https://docs.docker.com/storage/bind-mounts/), поэтому поддерживается hot-reload файлов Python.

Управление зависимостями - через [pip-tools](https://github.com/jazzband/pip-tools):
- Новая библиотека добавляется в `requirements.in`, поддерживается опциональное ограничение версий
- Запускается команда `pip-compile ...` (полная версия в начале файла `requirements.txt`)
- В результате работы команды обновляется файл зависимостей `requirements.txt`
- При перезапуске проекта через `docker compose up -d --build` новые зависимости устанавливаются автоматически внутри образа

## Загрузка локаций через команду

Для автоматизации добавления новых мест можно использовать команду

``` Bash
python manage.py load_place <url-to-json>
```

[Пример файла](https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%AF%D0%BF%D0%BE%D0%BD%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%B0%D0%B4.json), который может быть таким образом загружен.

---

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).

Frontend - [источник](https://github.com/devmanorg/where-to-go-frontend/blob/master/README.md).
