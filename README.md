# REST API "Оборудование"
Данный проект представляет собой REST API интерфейс для работы с сущностями "Оборудование" и "Типы оборудования".

## Используемые технологии
+ Python
+ Django
+ MySQL
+ Docker

## Установка и запуск
1. Склонировать репозиторий на локальную машину
```bash
git clone https://github.com/sp-va/networkHardware.git
cd networkHardware
```
2. Создать файл .env по образцу файла example.env, расположенного в рабочей директории.

3. Запустить проект:
```bash
docker-compose up --build
```

4. После запуск сервер приложение доступно по адресу http://localhost:8000.