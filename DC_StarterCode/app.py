import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

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

@app.route("/videogame")
def video_game_data():

    results = db.session.query(video_game.Name, video_game.Platform, video_game.Year, video_game.Genre, video_game.Publisher, video_game.NA_Sales, video_game.EU_Sales, video_game.JP_Sales, video_game.Other_Sales, video_game.Global_Sales).all()

    # Create lists from the query results
    video_game_name = [result[0] for result in results]
    video_game_platform = [result[1] for result in results]
    video_game_year = [result[2] for result in results]
    video_game_genre = [result[3] for result in results]
    video_game_publisher = [result[4] for result in results]
    video_game_na_sales = [result[5] for result in results]
    video_game_eu_sales = [result[6] for result in results]
    video_game_jp_sales = [result[7] for result in results]
    video_game_other_sales = [result[8] for result in results]
    video_game_global_sales = [result[9] for result in results]

    data_dict = {
        "Name": video_game_name,
        "Platform": video_game_platform,
        "Year" : video_game_year,
        "Genre" : video_game_genre,
        "Publisher" : video_game_publisher,
        "NA_Sales" : video_game_na_sales,
        "EU_Sales" : video_game_eu_sales,
        "JP_Sales" : video_game_jp_sales,
        "Other_Sales" : video_game_other_sales,
        "Global_Sales" : video_game_global_sales

    }

    # trace ={
    #     "x": video_game_year,
    #     "y": video_game_na_sales,
    #     "type": "bar"
    # }

    return jsonify(data_dict)


if __name__ == "__main__":
    app.run()
