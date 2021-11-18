from flask import Flask, render_template, request, url_for, flash, redirect
import os, datetime
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import abort

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))

app = Flask('__name__')
app.config['SECRET_KEY'] = 'your secret key'
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)


class Formulário(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    nome = db.Column(db.String(80), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)


@app.route('/')
def index():
       return render_template('index.html',)


@app.route('/responsaveis')
def responsaveis():
    return render_template('responsaveis.html')


@app.route('/escola')
def escola():
    return render_template('escola.html')


@app.route('/transportador')
def transportador():
    return render_template('transportador.html')
