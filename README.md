# Сервис Bewise Audio API

<img src="https://play-lh.googleusercontent.com/m2d1Cwc3c-yYGL1o4sgUSy-R0QaYLkmH3PVdBRaiLEVLlhF1ws3q-KP5opuSTTUIhx0" width=128>

Тестовое задание для компании ***Bewise.ai.*** API сервис для конвертации аудио из wav в mp3.

Данный сервис предоставляет возможности упрощённой регистрации, конвертации и скачивания аудио, хранения записей в БД.

### Чтобы запустить:

Клонируйте репозиторий в директорию, из которой будете запускать проект:

```BASH
git clone git@github.com:Ferdinand-I/bewise_audio_api.git
```

Перейдите в директорию проекта:

```BASH
cd bewise_audio_api/
```

Проект собран и работает в контейнерах Docker, чтобы их запустить выполните следующую команду:

```BASH
docker compose up
```

Ура! Сервис запущен локально и готов к работе!

Эндпоинт для регистрации:

http://localhost:8000/api/v1/user/

Чтобы пройти регистрацию, на указанный выше эндпоинт надо отправить POST-запрос следующего вида:

```JSON
{"username": "<username>"}
```

В ответе вы получите уникальные uuid-токен доступа и id для последующей работы с ресурсами.

Сконвертировать аудио из wav в mp3 можно сделав POST-запрос вида:

```JSON
{
  "user_id": "<int>",
  "user_uuid_token": "<int>",
  "audio": "<*.wav>"
}
```

на эндпоинт:

http://localhost:8000/api/v1/record/

В случае успеха в ответе вам вернётся ссылка для скачивания сконвертированного файла.

Посмотреть записи БД в контейнере можно. Открываем интерактивный терминал в контейнере:
  
```BASH
docker exec -ti BewiseAudioDB bash
```
  
Работает, как с обычной БД POstgreSQL.
Открываем консоль psql под пользователем "postgres":
  
```BASH
psql -U postgres
```

Коннектимся к БД:

```BASH
\c postgres
```

Выбираем все записи из таблицы с аудио:

```BASH
SELECT * FROM api_audiomodel;
```

