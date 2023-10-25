from flask import Blueprint,Flask,redirect,url_for,render_template
lab2 = Blueprint('lab2',__name__)


@lab2.route("/lab2/example")
def example():
    name = 'Шкуропатова Екатерина Александровна'
    number_lab = '2'
    group = 'ФБИ-13'
    number_course = '3'
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321},
    ]
    books = [
        {'author': 'Виктор Гюго', 'name': 'Собор Парижской Богоматери', 'genre': 'Роман', 'pages': 500},
        {'author': 'Анна Франк', 'name': 'Дневник Анны Франк', 'genre': 'Автобиография', 'pages': 280},
        {'author': 'Эмили Бронте', 'name': 'Грозовой перевал', 'genre': 'Роман', 'pages': 416},
        {'author': 'Михаил Булгаков', 'name': 'Мастер и Маргарита', 'genre': 'Роман', 'pages': 400},
        {'author': 'Даниель Дефо', 'name': 'Робинзон Крузо', 'genre': 'Роман', 'pages': 96},
        {'author': 'Маринина Александра', 'name': 'Иллюзия греха', 'genre': 'Детектив', 'pages': 448},
        {'author': 'Ремарк Эрих Мария', 'name': 'Три товарища', 'genre': 'Роман', 'pages': 480},
        {'author': 'Гоголь Николай', 'name': 'Ревизор', 'genre': 'Комедия', 'pages': 192},
        {'author': 'Достоевский Фёдор', 'name': 'Преступление и наказание', 'genre': 'Роман', 'pages': 592},
        {'author': 'Пушкин Александр', 'name': 'Пиковая дама', 'genre': 'Повесть', 'pages': 224},
    ]

    return render_template('example.html', name=name, number_lab=number_lab,
            group=group, number_course=number_course, fruits=fruits, books=books)


@lab2.route("/lab2/")
def lab():
    return render_template('lab2.html')


@lab2.route("/lab2/flowers_m")
def cat_breeds():
    name = 'Шкуропатова Екатерина Александровна'
    number_lab = '2'
    group = 'ФБИ-13'
    number_course = '3'

    return render_template('flowers_m.html', name=name, number_lab=number_lab,
            group=group, number_course=number_course)
