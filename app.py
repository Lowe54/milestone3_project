import os
import pymongo
from flask_pymongo import PyMongo
from flask import Flask, render_template,request,redirect,url_for
from bson.objectid import ObjectId
import json

app = Flask(__name__)

# client = pymongo.MongoClient("mongodb+srv://root:"+os.getenv('PASSWORD')+"@milestone4db-c4m84.mongodb.net/recipie_db?retryWrites=true")
app.config["MONGO_DB_NAME"] = 'recipie_db'
if __name__ == '__main__':
    app.config["MONGO_URI"] = "mongodb+srv://root:os.getEnv(PASSWORD)@milestone4db-c4m84.mongodb.net/recipie_db?retryWrites=true"

app.config["MONGO_URI"] = "mongodb+srv://root:Will0w2L11@milestone4db-c4m84.mongodb.net/recipie_db?retryWrites=true"


mongo = PyMongo(app)
@app.route('/')

def index():
    '''
    Function that defines the index page
    '''
    title = "The index page"
    return render_template('index.html', title=title)

@app.route('/form')
def form():
    '''
    @arg - edit =  Determines if the page loads current record information
    @arg - id = Only used in edit mode, it is used to grab the record data
    '''
    if request.args.get('edit') and request.args.get('id'):
        record_id = request.args.get('id')
        enable_edit_mode = request.args.get('edit')
    else:
        enable_edit_mode = '0'
        record_id = ''

    allerginlist = [ "Gluten", "Crustacean", "Eggs", "Fish", "Peanuts", "Soybeans", "Milk", "Nuts", "Celery", "Mustard", "Sesame", "Lupin", "Molluscs"]
    return render_template('form.html', edit=enable_edit_mode, id=record_id, allerginlist=allerginlist)

@app.route('/submit', methods=["POST", "GET"])
def submit():
    title = request.form.get('recipie_title')
    instructions = request.form.get('recipie_instructions')
    ingredients = request.form.get('recipie_ingredients')
    allergins = request.form.getlist('recipie_allergins')

    data = {"recipie_title": title, "recipie_instructions":instructions, "recipie_ingredients": ingredients,"recipie_allergins": allergins}
    recipies = mongo.db.recipies
    recipies.insert_one(data, bypass_document_validation=True)
    return redirect('/results/')

#Results page
@app.route('/results/')
def results():
    '''
    Results page
        @arg - page = The current page number
        @arg - sr = The start index for the results page, 20 means that it will start at index 20
    '''
    #Check to see if any parameters are defined
    if request.args.get('page'):
        page = int(request.args.get('page'))
        sr = int(request.args.get('sr'))
        currentpagenum = int(page)
    #If not, assign the default values
    else:
        page = 0
        sr = 0
        currentpagenum = 0  

    #TODO : Change this to fetch information from the DB
    #resultnum = ['Joseph Allen', 'Autumn Welch', 'Valerie Fields', 'Margaret Mccarty', 'Patricia Yu', 'Kelsey Burton', 'Charles Chandler', 'Michelle Washington', 'Wendy Morris', 'Sherri Perez', 'Holly Campbell', 'Karen Cisneros MD', 'Jessica Perry', 'Kimberly Miranda', 'Michael Lawrence']
    resultnum = mongo.db.recipies.find()
    
    pagecount = 0
    #We set the number to 11, since it is 0 based indexing, otherwise it only shows 9 results
    if len(resultnum) < 11:
        print("No need for extra pages here")
    else:
        #Determine the number of result pages
        pages = int(len(resultnum) / 11)
        if pages == 0:
            pagecount = pages
            
        else:
            pagecount = pages + 1
            
      
    return render_template('results.html', results=resultnum, c_page=currentpagenum, pc=pagecount, pages=pages, sr=sr, nh=10)
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=False)