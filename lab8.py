# Импорт необходимых модулей Flask
from flask import Blueprint, render_template, request, abort, jsonify
from datetime import datetime

# Создание Blueprint с именем "lab8"
lab8 = Blueprint('lab8', __name__)

# Маршрут для отображения главной страницы
@lab8.route('/lab8/')
def main():
    return render_template('lab8/index.html')
