from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy in-memory storage (replace later with database)
menu_items = []
notifications = []

@app.route('/')
def home():
    return "Welcome to Chatori Gully Food Delivery App!"

@app.route('/admin')
def admin():
    return render_template('admin.html', notifications=notifications)

@app.route('/restaurant')
def restaurant():
    return render_template('restaurant.html', menu_items=menu_items)

@app.route('/customer')
def customer():
    return render_template('customer.html', menu_items=menu_items)

@app.route('/add_item', methods=['POST'])
def add_item():
    name = request.form['name']
    price = int(request.form['price'])
    status = 'pending' if price > 200 else 'approved'
    menu_items.append({'name': name, 'price': price, 'status': status})
    return redirect(url_for('restaurant'))

@app.route('/send_notification', methods=['POST'])
def send_notification():
    message = request.form['message']
    notifications.append(message)
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run()
