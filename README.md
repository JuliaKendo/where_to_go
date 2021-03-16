# Куда пойти в Москве

Веб-сайт показывает значимые места на карте Москвы. Куда пойти, что посмотреть, где отдохнуть. Сайт можно посмотреть по ссылке [juliakendo.pythonanywhere.com](https://juliakendo.pythonanywhere.com/)

<img src="screenshots/site.png">

## Как установить

Для запуска сайта вам понадобится Python третьей версии.

Скачайте код с GitHub. 
Перед установкой рекомендуется создать виртуальное окружение.

Установите зависимости:

```sh
pip install -r requirements.txt
```

Создайте базу данных SQLite

```sh
python3 manage.py migrate
```

Для доступа в админку выполните 

```sh
python3 manage.py createsuperuser
```


## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 4 переменные:
- `DEBUG` — дебаг-режим. Поставьте `1`, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
- `DATABASE_FILEPATH` — полный путь к файлу базы данных SQLite, например: `/home/user/db.sqlite3`
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)


## Как запустить локально

Запустите сервер:

```sh
python3 manage.py runserver
```

Откройте в браузере [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Как заполнять

Откройте админку сайта в браузере [juliakendo.pythonanywhere.com/admin](https://juliakendo.pythonanywhere.com/admin). Добавляйте новые локации, заполняйте описания, их координаты и изображения.

Для быстрого заполнения предусмотрена загрузка данных из json файлов:

```sh
python3 manage.py load_place "https://адрес_файла/имя_файла.json"
```

Файл json должен быть следующего формата:

```json
{
    "title": "Экскурсионный проект «Крыши24.рф»",
    "imgs": [
        "https://kudago.com/media/images/place/d0/f6/d0f665a80d1d8d110826ba797569df02.jpg",
        "https://kudago.com/media/images/place/66/23/6623e6c8e93727c9b0bb198972d9e9fa.jpg",
        "https://kudago.com/media/images/place/64/82/64827b20010de8430bfc4fb14e786c19.jpg",
    ],
    "description_short": "Хотите увидеть Москву с высоты птичьего полёта?",
    "description_long": "<p>Проект «Крыши24.рф» проводит экскурсии ...</p>",
    "coordinates": {
        "lat": 55.753676,
        "lng": 37.64
    }
}
```

Тестовые данные для заполнения сайта получены с [https://github.com/devmanorg/where-to-go-places](https://github.com/devmanorg/where-to-go-places)

## Настройки

Внизу слева на странице можно включить отладочный режим.

<img src="screenshots/debug-option.png">

Если что-то работает не так, как ожидалось, то начните с включения отладочного режима логирования.


## Используемые библиотеки

* [Leaflet](https://leafletjs.com/) — отрисовка карты
* [loglevel](https://www.npmjs.com/package/loglevel) для логгирования
* [Bootstrap](https://getbootstrap.com/) — CSS библиотека
* [Vue.js](https://ru.vuejs.org/) — реактивные шаблоны на фронтенде

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
