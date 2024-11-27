# Тестовое задание

Тестовое задание реализовано в полном объёме, код реализации view расположен в restaurant/veiws.py.

Технологический стек: python==3.12.4, Django\DRF==latest.

Ньюансы:
- для удобства оценки задания есть скрпт заполнения БД тестовыми данными 
(**_python manage.py test_data_**), который создаёт:
  -  2 категории - Напитки и Выпечка (в каждой категории по 2 блюда 
(Чай, Газировка и Булочка, Сметанник). Газировка и Сметанник имеют параметр is_publish 
в значении False, соответственно, при запросе не выводятся;
  -  1 категорию - Мясо (в этой категории 2 блюда, оба имеют параметр is_publish 
в значении False, соответственно, категория при запросе не выводится);
  -  1 категорию - Другое (в этой категории нет блюд, соответственно, категория при запросе не выводится).

---
### Quickstart

После установки и активации виртуального окружения выполните следующие команды:

- `pip install -r requirements.txt`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py test_data`
- `python manage.py runserver`

URL - 127.0.0.1/api/v1/foods/

