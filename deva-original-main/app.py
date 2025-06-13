from flask import Flask, render_template, request, redirect, url_for,session,flash
import mysql.connector
from datetime import datetime


app = Flask(__name__)
app.secret_key="1a2s3we4r89e2sa4"
# # MySQL Configuration
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="college_events"
)
cursor = conn.cursor()
print(cursor)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/events")
def events():
    return render_template("event.html")

@app.route("/add", methods=["GET", "POST"])
def add_event():
    if request.method == "POST":
        name = request.form["name"]
        date = request.form["date"]
        time = request.form["time"]
        venue = request.form["venue"]
        category = request.form["category"]
        description = request.form["description"]

        query = "INSERT INTO events (name, date, time, venue, category, description) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (name, date, time, venue, category, description)
        cursor.execute(query, values)
        conn.commit()

        return "Event submitted successfully!"
    return render_template("add.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin@123' and password == '1234':
            return redirect(url_for('add_event'))
        else:
            return render_template("login1.html")
            flash('Invalid username or password', 'error')

    
    return render_template("login1.html")

@app.route('/login1')
def login1():
    return render_template('login.html')

@app.route("/about")
def about():
    return render_template("abt.html")

if __name__ == "__main__":
    app.run()
