FastAPI проект с возможностью авторизации. Для создания пользователя в БД необходимо выполнить команду ```python create_user.py``` и ввести имя пользователя и пароль в консоли после выполнения всех шагов.

Порядок запуска:
1) Открыть консоль (командную строку на Windows) и клонировать проект ```git clone https://github.com/kyarmakov/FastAPI```
2) Перейти в папку проекта ```cd FastAPI```
3) Создать виртуальное окружение для избежания конфликтов версий ```python -m venv .venv``` для Windows и ```python3 -m venv .venv``` для Linux и Mac.
4) Активировать виртуальное окружение. Для Windows ```.venv\Scripts\activate``` . Для Linux/Mac ```source .venv/bin/activate```
5) Выполнить команду ```pip install -r requirements.txt``` для установки зависимостей.
6) Запустить проект ```uvicorn carsharing:app```
7) Перейти по адресу ```http://localhost:8000```

Документация находится по адресу ```http://localhost:8000/docs```
