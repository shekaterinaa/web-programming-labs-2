from flask import Blueprint, redirect, url_for, render_template
lab1 = Blueprint('lab1', __name__)

@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect ("/menu", code=302)

@lab1.route("/menu")
def menu():
    return '''
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
'''

@lab1.route("/lab1")
def lab1():
    return '''
<!doctype html>
<link rel ="stylesheet href="''' + url_for('static',filename='lab1.css') + '''">
<html>
    <head>
        <title> Шкуропатова Екатерина Александровна, лабораторная 1</title>
    </head>
    <body>
        <header>

           НГТУ, ФБ, Лабораторная работа 1

        </header>
        <h1>web-сервер на flask</h1>

            <div>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности
            </div>
            <a href="http://127.0.0.1:5000/menu" target="_blank">Меню</a>
            <h2>Реализованные роуты</h2>
            <li><a href="http://127.0.0.1:5000/lab1/oak" target="_blank">Дуб</a></li>
            <li><a href="http://127.0.0.1:5000/lab1/student" target="_blank">Студент</a></li>
            <li><a href="http://127.0.0.1:5000/lab1/python" target="_blank">Python</a></li>
            <li><a href="http://127.0.0.1:5000/lab1/shpitz" target="_blank">Шпиц</a></li>
        </main>

        <footer>
            &copy; Шкуропатова Екатерина, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
</html>
'''
@lab1.route('/lab1/oak')
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
@lab1.route('/lab1/student')
def student():
    return '''
<!doctype html>
<link rel="stylesheet" href="''' +  url_for('static', filename='lab1.css') + '''">
<html>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
        <h1>Шкуропатова Екатерина Александровна</h1>
        <img src="''' +  url_for('static', filename='logo_ngtu.png') + '''">
        <footer>
            &copy; Шкуропатова Екатерина, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
</html>
'''
@lab1.route('/lab1/python')
def python():
    return '''
<!doctype html>
<link rel="stylesheet" href="''' +  url_for('static', filename='lab1.css') + '''">
<html>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
        <main>
            <h1>Python</h1>
            <div>
            Высокоуровневый язык программирования общего назначения с динамической строгой типизацией
            и автоматическим управлением памятью, ориентированный на повышение производительности разработчика,
            читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ.
            Язык является полностью объектно-ориентированным в том плане, что всё является объектами. 
            Необычной особенностью языка является выделение блоков кода пробельными отступами. 
            Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает необходимость обращаться к документации. 
            </div>
            <h2>Преимущества Питон</h2>
            
            <li>Это интерпретируемый язык. До запуска программа на Python представляет собой обычный текстовый файл, 
            который можно запустить на любой платформе, где установлен интерпретатор.</li>
            <li>Он отлично подходит новичкам. Python хорошо спроектирован и логичен.
             Для его изучения даже не нужно знать английский язык. 
             Благодаря его простоте разработка идёт намного быстрее, потому что программист пишет меньше кода.</li>
            <li>У языка мощное сообщество. Сообщество пользователей Python настолько большое, что если вы столкнётесь 
            с непонятной ошибкой, то, скорее всего, быстро найдёте её решение в интернете. 
            Ведь до вас кто-то уже столкнулся с похожей и выложил решение на Stack Overflow.</li>
            
            
        </main>
        
        <img src="''' +  url_for('static', filename='python.png') + '''">
        <footer>
            &copy; Шкуропатова Екатерина, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@lab1.route('/lab1/shpitz')
def shpitz():
    return '''
<!doctype html>
<link rel="stylesheet" href="''' +  url_for('static', filename='lab1.css') + '''">
<html>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
        <h1>Шпиц (породы собак) </h1>
        <div>
        Исследователи утверждают, что предками ныне известных шпицев были свайные и торфяные собаки.
        А самый распространённый среди собаководов померанский шпиц жил ещё в Древнем Египте.
        Сначала порода шпиц служила людям в качестве охранников, и только потом собачки стали декоративными членами семьи.
        А так как селекционные работы велись во многих странах мира, сейчас мы имеем самые разные виды породы шпиц.
        </div>
        <div>
       В международной кинологической классификации шпицами принято называть отельную группу собак,
       отличающихся общими особенностями экстерьера – заостренная форма ушей,
       закрученный в кольцо хвост и плотная двойная шерстка. 
        </div>
        <img src="''' +  url_for('static', filename='shpitz.png') + '''">
        <footer>
            &copy; Шкуропатова Екатерина, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
</html>

'''