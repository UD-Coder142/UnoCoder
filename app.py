from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'endxskuifxndiinmenxmeibdgedidg'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1000))
    sender = db.Column(db.String(50))
    room = db.Column(db.Integer, db.ForeignKey('room.id'))

    def __repr__(self):
        return "<Name %r>" % self.id

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roomname = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(20))
    messages = db.relationship('Chat')

    def __repr__(self):
        return "<Name %r>" % self.id

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form['Room']

        if data:
            flash("Room Found!")
        else:
            return redirect(url_for('add'))
    
    return render_template('index.html')

@app.route('/rooms/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = request.form['Room']
    
    return render_template('add.html')