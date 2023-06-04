# Тестовое задание на курс «Python»
## Описание задачи
Реализуйте REST-сервис просмотра текущей зарплаты и даты следующего
повышения. Из-за того, что такие данные очень важны и критичны, каждый
сотрудник может видеть только свою сумму. Для обеспечения безопасности, вам
потребуется реализовать метод где по логину и паролю сотрудника будет выдан
секретный токен, который действует в течение определенного времени. Запрос
данных о зарплате должен выдаваться только при предъявлении валидного токена.
## Реализованные необязательные технические требования
- зависимости зафиксированы менеджером зависимостей poetry
- возможность собирать и запускать контейнер с сервисом в Docker
## Первый вариант запуска
```sh
docker compose up
docker compose exec web alembic upgrade head
```
### _Ссылки_
- http://localhost:8008/admin admin / admin
- http://localhost:8008/docs
- http://localhost:8008/redoc

## Второй вариант запуска
```sh
docker compose -f docker-compose.db.yml up
pip install --upgrade pip
pip install poetry
cd app
poetry install
poetry shell
alembic upgrade head
uvicorn main:app
```
### _Ссылки_
- http://localhost:8000/admin admin / admin
- http://localhost:8000/docs
- http://localhost:8000/redoc
