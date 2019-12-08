from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

project_dir = os.path.dirname(os.path.abspath(__file__))
dataBase_file = "sqlite:///{}".format(
    os.path.join(project_dir, "schoolDatabase.db"))

app.config['SQLALCHEMY_DATABASE_URI'] = dataBase_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# db.create_all()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    userName = db.Column(db.String(30), unique=False, nullable=False)
    mobile = db.Column(db.Integer, unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False)
    password = db.Column(db.String(20), unique=True, nullable=False)
    gender = db.Column(db.String(10))
    joining_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.id
# db.create_all()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register')
def teacher():
    return render_template('register.html')


@app.route('/addTeacher', methods=['POST','GET'])
def admin():
    if request.method == 'POST':
        myteacher = Users()

        myteacher.userName = request.form['Username']
        myteacher.mobile = request.form['cell_no']
        myteacher.email = request.form['email']
        myteacher.password = request.form['password']
        myteacher.gender = request.form['gender']
        try:
            db.session.add(myteacher)
            db.session.commit()
            return redirect('/register')
        except:
            return 'Not getting data from html form'
 
    else:
        return "<h1>method not post</h1>"


if __name__ == '__main__':
    app.run(debug=True)
