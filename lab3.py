from flask import Blueprint,render_template,request
lab3 = Blueprint('lab3',__name__)

@lab3.route("/lab3/")
def lab():
    return render_template('lab3.html')

@lab3.route("/lab3/forml")
def forml():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'

    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'

    sex = request.args.get('sex')
    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors)

@lab3.route("/lab3/order")
def order():
    return render_template('order.html')

@lab3.route("/lab3/pay")
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
       price = 80
    else:
       price = 70 

    if request.args.get('milk') == 'on':
       price += 30
    if request.args.get('sugar') == 'on':
       price += 10

    return render_template('pay.html', price = price)  

@lab3.route("/lab3/sps")
def sps():

    return render_template('sps.html')


@lab3.route('/lab3/ticket')
def ticket():
   errors = {}
   user = request.args.get('user')
   type = request.args.get('type')
   shelf = request.args.get('shelf')
   age = request.args.get('age')
   Destination = request.args.get('Destination')
   bag = request.args.get('bag')
   date = request.args.get('date')
   Departure_point = request.args.get('Departure_point')
   return render_template('ticket.html', user=user, type=type, shelf=shelf, age=age, Departure_point=Departure_point, Destination=Destination, date=date, bag=bag)

@lab3.route('/lab3/pay_ticket')
def pay_ticket():
   user = request.args.get('user')
   shelf = request.args.get('shelf')
   age = request.args.get('age')
   Destination = request.args.get('Destination')
   bag = request.args.get('bag')
   date = request.args.get('date')
   Departure_point = request.args.get('Departure_point')
   type = request.args.get('type')
   return render_template('pay_ticket.html', user=user, type=type, shelf=shelf, age=age, Departure_point=Departure_point, Destination=Destination, date=date, bag=bag)
