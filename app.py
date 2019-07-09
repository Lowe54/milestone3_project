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
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

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
        enable_edit_mode = False
        record_id = ''
    rec = None
    if enable_edit_mode:
        rec = mongo.db.recipies.find_one({"_id": ObjectId(record_id)})
        print(rec)
        
    allerginlist = [ "Gluten", "Crustacean", "Eggs", "Fish", "Peanuts", "Soybeans", "Milk", "Nuts", "Celery", "Mustard", "Sesame", "Lupin", "Molluscs"]
    return render_template('form.html', edit=enable_edit_mode, id=record_id, allerginlist=allerginlist,recipie=rec)

@app.route('/submit', methods=["POST", "GET"])
def submit():
    title = request.form.get('recipie_title')
    description = request.form.get('recipie_description')
    instructions = request.form.get('recipie_instructions')
    ingredients = request.form.get('recipie_ingredients')
    allergins = request.form.getlist('recipie_allergins')
    recipie_id = request.form.get('recipie_id')
    data = {"recipie_title": title, "recipie_description": description, "recipie_instructions":instructions, "recipie_ingredients": ingredients,"recipie_allergins": allergins}
    print (recipie_id)
    recipies = mongo.db.recipies
    if not recipie_id:
        recipies.insert_one(data)
        return redirect('/results/')
    else:
        print("Else Statement")
        recipies.update({"_id": ObjectId(recipie_id)}, data)
        return redirect('/results/')

#Results page
@app.route('/results/')
def results():
    '''
    Results page
        @arg - page = The current page number
        @arg - sr = The start index for the results page, 20 means that it will start at index 20
        @arg - qt = The query term
    '''
    filterOptions = []
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
    results = []
    if request.args.get('qt'):
        query = request.args.get('qt')
        print(query)
        #Check for allergin filter
        if request.args.get('allergin'):
            allergin = request.args.get('allergin')
            filterOptions.append(allergin)
            recipies = mongo.db.recipies.find({"$text": { "$search": query },"recipie_allergins": {"$nin" : [allergin] } })
            for r in recipies:
                results.append(r)
        else:
            # Commented out for now, needs to be fixed
            # if request.args.get('allergin').len > 1:
            #     print ("More than one allergin selected")
            #     selectedallergin = []
            #     for a in request.args.get('allergin'):
            #         selectedallergin.append(a)
            #         filterOptions.append(a)
            #         recipies = mongo.db.recipies.find({"$text": { "$search": query },"recipie_allergins": {"$nin" : selectedallergin } })
            #         for r in recipies:
            #             results.append(r)
            # else:
            recipies = mongo.db.recipies.find( { "$text": { "$search": query } })
            for r in recipies:
                results.append(r)
    else:
        query = ''
        recipies = mongo.db.recipies.find()
        for r in recipies:
            results.append(r)

    #FilterList
    
    allerginlist = [ "Gluten", "Crustacean", "Eggs", "Fish", "Peanuts", "Soybeans", "Milk", "Nuts", "Celery", "Mustard", "Sesame", "Lupin", "Molluscs"]
    pagecount = 0
    #We set the number to 11, since it is 0 based indexing, otherwise it only shows 9 results
    if len(results) < 11:
        print("No need for extra pages here")
        pages = 0
    else:
        #Determine the number of result pages
        pages = int(len(results) / 11)
        if pages == 0:
            pagecount = pages
            
        else:
            pagecount = pages + 1
            
      
    return render_template('results.html',currentQueryTerm=query,allerginList=allerginlist, selectedFilters=filterOptions, results=results, c_page=currentpagenum, pc=pagecount, pages=pages, sr=sr, nh=10, maxresults=len(results))

@app.route('/recipie')
def recipie():
    error = None
    if request.args.get('id'):
        record_id = request.args.get('id')
        rec = mongo.db.recipies.find_one({"_id": ObjectId(record_id)})
        return render_template('recipie.html', recipie=rec)

    else:
        error = 'No recipie found'
        return render_template('index.html', error=error)

@app.route('/addLike', methods=['GET','POST'])
def addLike():
    record_id = request.args.get('recordID')
    recipies = mongo.db.recipies
    
    
    recipies.update({'_id': ObjectId(record_id)}, {'$inc': {'likes': int(1)}})
    
    return "Successfully added like"

@app.route('/addDislike', methods=['GET','POST'])
def addDislike():
    record_id = request.args.get('recordID')
    recipies = mongo.db.recipies
    
    
    recipies.update({'_id': ObjectId(record_id)}, {'$inc': {'dislikes': int(1)}})
    
    return "Successfully added dislike"
      
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=False)