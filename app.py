import os
import pymongo
from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://root:"+os.getenv('PASSWORD')+"@milestone4db-c4m84.mongodb.net/recipie_db?retryWrites=true")
db = client.test

@app.route('/')
def index():
    title = "The index page"
    return render_template('index.html', title=title)


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=False)