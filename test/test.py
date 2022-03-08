import math
from flask import session
from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import json

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True
app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD = params['gmail-password']
)
mail = Mail(app)
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)
class Contacts(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    fName = db.Column(db.String(50), nullable=False)
    lName = db.Column(db.String(50), nullable=False)
    password=db.Column(db.String(20), nullable=False)
    number = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(20), nullable=False)
@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        '''Add entry to the database'''
        fName = request.form.get('fName')
        lName=request.form.get('lName')
        email = request.form.get('email')
        password=request.form.get('password')
        number = request.form.get('number')
        entry = Contacts(fName=fName,lName=lName,number= number,password=password,email = email )
        db.session.add(entry)
        db.session.commit()

        mail.send_message('New message from= '+ fName,
        sender = email,
        recipients = [params['gmail-user']],
        body =  number,
    )
    return render_template('contact.html',params=params)
