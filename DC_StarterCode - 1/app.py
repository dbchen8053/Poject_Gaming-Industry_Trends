import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.sql import func

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
# import json

app = Flask(__name__)


#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/Sales.sqlite"
db = SQLAlchemy(app)

class video_game(db.Model):
    __tablename__ = 'Sales_table'

    Rank = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String)
    Platform = db.Column(db.String)
    Year = db.Column(db.Integer)
    Genre = db.Column(db.String)
    Publisher = db.Column(db.String)
    NA_Sales = db.Column(db.Integer)
    EU_Sales = db.Column(db.Integer)
    JP_Sales = db.Column(db.Integer)
    Other_Sales = db.Column(db.Integer)
    Global_Sales = db.Column(db.Integer)

    # def __repr__(self):
    #     return '<Emoji %r>' % (self.name)




@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/NA_sales_year")
def NA_sales_year_data():
    results = db.session.query(video_game.Year, func.sum(video_game.NA_Sales)).group_by(video_game.Year).all()
    video_game_year = [result[0] for result in results]
    video_game_na_sales_year = [result[1] for result in results]

    trace = {
        "x": video_game_year,
        "y": video_game_na_sales_year,
        "type": "bar",
        "marker": {"color": "blue"}

    }
    return jsonify(trace)

@app.route("/EU_sales_year")
def EU_sales_year_data():
    results = db.session.query(video_game.Year, func.sum(video_game.EU_Sales)).group_by(video_game.Year).all()
    video_game_year = [result[0] for result in results]
    video_game_eu_sales_year = [result[1] for result in results]

    trace = {
        "x": video_game_year,
        "y": video_game_eu_sales_year,
        "type": "bar",
        "marker": {"color": "orange"}

    }
    return jsonify(trace)

@app.route("/JP_sales_year")
def JP_sales_year_data():
    results = db.session.query(video_game.Year, func.sum(video_game.JP_Sales)).group_by(video_game.Year).all()
    video_game_year = [result[0] for result in results]
    video_game_jp_sales_year = [result[1] for result in results]

    trace = {
        "x": video_game_year,
        "y": video_game_jp_sales_year,
        "type": "bar",
        "marker": {"color": "green"}

    }
    return jsonify(trace)

@app.route("/Other_sales_year")
def Other_sales_year_data():
    results = db.session.query(video_game.Year, func.sum(video_game.Other_Sales)).group_by(video_game.Year).all()
    video_game_year = [result[0] for result in results]
    video_game_other_sales_year = [result[1] for result in results]

    trace = {
        "x": video_game_year,
        "y": video_game_other_sales_year,
        "type": "bar",
        "marker": {"color": "red"}

    }
    return jsonify(trace)

@app.route("/Global_sales_year")
def Global_sales_year_data():
    results = db.session.query(video_game.Year, func.sum(video_game.Global_Sales)).group_by(video_game.Year).all()
    video_game_year = [result[0] for result in results]
    video_game_global_sales_year = [result[1] for result in results]

    trace = {
        "x": video_game_year,
        "y": video_game_global_sales_year,
        "type": "bar",
        "marker": {"color": "black"}

    }
    return jsonify(trace)



@app.route("/videogame")
def video_game_data():

    results = db.session.query(video_game.Year, func.sum(video_game.NA_Sales), func.sum(video_game.EU_Sales), func.sum(video_game.JP_Sales), func.sum(video_game.Other_Sales), func.sum(video_game.Global_Sales)).group_by(video_game.Year).all()

    video_game_year = [result[0] for result in results]
    video_game_na_sales_year = [result[1] for result in results]
    video_game_eu_sales_year = [result[2] for result in results]
    video_game_jp_sales_year = [result[3] for result in results]
    video_game_other_sales_year = [result[4] for result in results]
    video_game_global_sales_year = [result[5] for result in results]

    data_dict = {
        "Year" : video_game_year,
        "NA_Sales" : video_game_na_sales_year,
        "EU_Sales" : video_game_eu_sales_year,
        "JP_Sales" : video_game_jp_sales_year,
        "Other_Sales" : video_game_other_sales_year,
        "Global_Sales" : video_game_global_sales_year

    }



    return jsonify(data_dict)

@app.route("/genre")
def genre_year_data():
    results = db.session.query(video_game.Genre, func.count(video_game.Genre)).group_by(video_game.Genre).all()
    video_game_genre = [result[0] for result in results]
    video_game_genre_couont = [result[1] for result in results]

    trace = {
        "labels": video_game_genre,
        "values": video_game_genre_couont,
        "type": "pie"

    }
    return jsonify(trace)

@app.route("/publisher")
def publisher_year_data():
    results = db.session.query(video_game.Publisher, func.count(video_game.Publisher)).group_by(video_game.Publisher).order_by(func.count(video_game.Publisher).desc()).limit(10).all()
    video_game_publihser = [result[0] for result in results]
    video_game_publisher_couont = [result[1] for result in results]

    trace = {
        "x": video_game_publihser,
        "y": video_game_publisher_couont,
        # "marker": {"color": ["red", "orange", "yellow", "green", "blue", "purple", "black", "pink", "grey", "brown"]},
        "type": "bar"

    }
    return jsonify(trace)

@app.route("/platform")
def platfor_year_data():
    results = db.session.query(video_game.Platform, func.count(video_game.Platform)).group_by(video_game.Platform).order_by(func.count(video_game.Platform).desc()).limit(10).all()
    video_game_platform = [result[0] for result in results]
    video_game_platform_couont = [result[1] for result in results]

    trace = {
        "x": video_game_platform,
        "y": video_game_platform_couont,
        # "marker": {"color": ["red", "orange", "yellow", "green", "blue", "purple", "black", "pink", "grey", "brown"]},
        "type": "bar"

    }
    return jsonify(trace)



@app.route("/genre_year")
def genre_year_count_data():
    results = db.session.query(video_game.Year, video_game.Genre, func.count(video_game.Genre)).group_by(video_game.Genre, video_game.Year).all()
    # video_game_genre_year = [result[0] for result in results]
    # video_game_genre = [result[1] for result in results]
    # video_game_genre_couont = [result[2] for result in results]

    # data_dict = {
    #     "year": video_game_genre_year,
    #     "genre": video_game_genre,
    #     "genre count": video_game_genre_couont

    # }

    data_dict = [{'year': result[0], 'genre': result[1], 'genre_count': result[2]} for result in results]
    return jsonify(data_dict)


if __name__ == "__main__":
    app.run()
