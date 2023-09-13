from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
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
