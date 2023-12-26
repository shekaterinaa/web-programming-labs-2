from flask import Flask, redirect, url_for, render_template, session, request

from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab7 import lab7
from lab8 import lab8
from lab9 import lab9


app = Flask(__name__)

app.secret_key = "123"
user_db = "kate_knowledge_base"
host_ip = "127.0.0.1"
host_port = "5432"
database_name = "knowledge_base_for_kate"
password = "123"

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user_db}:{password}@{host_ip}:{host_port}/{database_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab7)
app.register_blueprint(lab8)
app.register_blueprint(lab9)

if __name__ == "__main__":
    app.run(debug=True)
    
    