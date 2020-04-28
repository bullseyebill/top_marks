import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'top_marks'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://ourAdmin:P00lly@cluster0-ljcl4.mongodb.net/top_marks?retryWrites=true&w=majority')

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_buoys')
def get_buoys():
    return render_template("buoys.html", buoys=mongo.db.buoys.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP','0.0.0.0'),
            port=int(os.environ.get('PORT','5000')),
            debug=True)  