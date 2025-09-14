from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # Landing page with role selection

@app.route("/login")
def login():
    role = request.args.get('role')
    return render_template("login.html", role=role)

@app.route("/dashboard", methods=['POST'])
def dashboard():
    phone = request.form.get('phone')
    role = request.form.get('role')
    return render_template("dashboard.html", role=role, phone=phone)

@app.route("/admin")
def admin_dashboard():
    return render_template("admin.html")

@app.route("/restaurant")
def restaurant_dashboard():
    return render_template("restaurant.html")

@app.route("/rider")
def rider_dashboard():
    return render_template("rider.html")

if __name__ == "__main__":
    app.run(debug=True)
