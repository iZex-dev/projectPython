<div id="header" align="center">
  <img src=https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWtjbHMyNGRzdXpqcmhodmo5bWhxdGMxNzVmd21ncGdtcGloMWVlciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/qgQUggAC3Pfv687qPC/giphy.gif width="250"/>
</div>

## :computer: Коротко о моем проекте:
В данном проекте будут реализованы домашние работы курса бекенд-разработчика школы SkyPro, в нем IT-отдел крупного банка делает новую фичу для личного кабинета клиента. Это виджет, который показывает несколько последних успешных банковских операций клиента. 

---

### 
<h1>
Установка
  <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHFlaGExcWQ3Ymx6em01NnRhNnU3eDNyenNmNHV4amZjeTdnM2oxNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/blCD7isAOkZ9DYisuU/giphy.gif" width="50px"/>
</h1>

1. Клонируйте репозиторий:


2. Установите зависимости:
poetry install

3. Создайте базу данных и выполните миграции:
python manage.py migrate

4. Запустите локальный сервер:
python manage.py runserver

5. Активировать окружение:
poetry shell

## 
<h1>
Использование:
  <img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjFkY3hpMmZsNGMwcnM5Ynl4Z2UybW0yOTZtNTlpM3J0dnFsNmVhYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/jdPMeyv9rn0hZHh8n9/giphy.gif"
width="60px"/>
</h1>
    
1. Перейдите на страницу в вашем веб-браузере.
2. Создайте новую учетную запись или войдите существующей.
3. Создайте новую запись в блоге или оставьте комментарий к существующей.

---

###
<h1>
Пример использования функций:
  <img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzRpcnhoYmk0a2FkczY5ejNmbmIxbnlzc2k3NjJncWR2NWs0aDk3dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/bLVTnQvgggksbDXs7S/giphy.gif'
width='60px'/>
</h1>

1. Функция get_mask_card_number:
```
7000792289606361     # входной аргумент
7000 79** **** 6361  # выход функции
```                    
3. Функция get_mask_account:
```
73654108430135874305  # входной аргумент
**4305  # выход функции
```
4. Функция mask_account_card:
```
# Пример для карты
Visa Platinum 7000792289606361  # входной аргумент
Visa Platinum 7000 79** **** 6361  # выход функции
# Пример для счета
Счет 73654108430135874305  # входной аргумент
Счет **4305  # выход функции
```
5. Функция get_date:
```
print(get_date("2025-06-14T12:00:00"))  # Вывод: 14.06.2025
```
6. Функция filter_by_state:
```
# Выход функции со статусом по умолчанию 'EXECUTED'
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
# Выход функции, если вторым аргументов передано 'CANCELED'
[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```
7. Функция sort_by_date:
```
# Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```
