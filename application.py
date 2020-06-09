import os

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask("cs50-project1-yp")

# Check for environment variable
if not os.getenv("postgres://emllsnhszfqing:76a579bd999dd5a058a4450f7aef9054688897f4db95917b9d57a1d1bfa7638f@ec2-18-210-214-86.compute-1.amazonaws.com:5432/dfht55lhd7uuvh"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("postgres://emllsnhszfqing:76a579bd999dd5a058a4450f7aef9054688897f4db95917b9d57a1d1bfa7638f@ec2-18-210-214-86.compute-1.amazonaws.com:5432/dfht55lhd7uuvh"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "Project 1: TODO"
