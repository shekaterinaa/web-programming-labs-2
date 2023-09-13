from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect ("/menu", code=302)

@app.route("/menu")
def menu():
    return """
<!doctype html>
<html>
    <head>
        <title> НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>
        <h1><a href="/lab1">Меню </a></h1>
        <footer>
            &copy; Шкуропатова Екатерина, ФБИ-13 , 3 курс, 2023
        </footer>
    </body>
</html>
"""

@app.route("/lab1")
def lab1():
    return """
<!doctype html>
<html>
    <head>
        <title> Шкуропатова Екатерина Александровна, лабораторная 1</title>
    </head>
    <body>
        <header>

           НГТУ, ФБ, Лабораторная работа 1

        </header>
        <h1>web-сервер на flask</h1>
        <footer>
            &copy; Шкуропатова Екатерина, ФБИ-13 , 3 курс, 2023
        </footer>
    </body>
</html>
"""
@app.route('/lab1/oak')
def oak():
    return '''
<!doctype html>
<html>
<head>
<link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
</head>
   <body>
      <h1>Дуб</h1>
      <div class="image-k"><img src="''' + url_for ('static', filename='oak.jpg') + '''"></div>
   </body>
<html>
'''
