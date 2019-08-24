import os
import pymongo
from flask_pymongo import PyMongo, MongoClient
from flask import Flask, flash, render_template, request, redirect, url_for
from bson.objectid import ObjectId
import json
import datetime
from testFramework import *
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config["MONGO_DB_NAME"] = 'recipie_db'
if __name__ == '__main__':
    app.config["MONGO_URI"] = f"mongodb+srv://root:{os.environ.get('PASSWORD')}@milestone4db-c4m84.mongodb.net/recipie_db?retryWrites=true"
    app.config["BASE_PATH"] = f"{os.environ.get('BASE_PATH')}"
else:
    app.config["MONGO_URI"] = "mongodb+srv://root:Will0w2L11@milestone4db-c4m84.mongodb.net/recipie_db?retryWrites=true"
    app.config["BASE_PATH"] = "./static/images"
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
# 3MB max file size
app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024
mongo = PyMongo(app)


@app.route('/')
def index():
    '''
    Function that defines the index page
    @arg error = Any error messages (no record etc..)
    '''
    title = "Welcome to the RecipieDB"
    recs = mongo.db.recipies.find().sort('likes', pymongo.DESCENDING)
    return render_template('index.html', title=title, recs=recs)


@app.route('/form')
def form():
    '''
    This page allows for the addition and editing of recipies
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
        title = "Edit a recipie|RecipieDB"
        rec = mongo.db.recipies.find_one({"_id": ObjectId(record_id)})
    else:
        title = "Add a recipie|RecipieDB"
    todaydate = datetime.datetime.now()
    allerginlist = ["Gluten", "Crustacean", "Eggs",
                    "Fish", "Peanuts", "Soybeans", "Milk", "Nuts",
                    "Celery", "Mustard", "Sesame", "Lupin", "Molluscs"]
    return render_template(
                        'form.html', title=title,
                        edit=enable_edit_mode, id=record_id,
                        allerginlist=allerginlist, recipie=rec,
                        date=todaydate)


@app.route('/submit', methods=["POST", "GET"])
def submit():
    '''
    Submission page
    This handles the information passed through from the form

    This contains automated testing to check the types of field are correct
    '''
    title = request.form.get('recipie_title')
    description = request.form.get('recipie_description')
    instructions = request.form.get('recipie_instructions')
    ingredients = request.form.get('recipie_ingredients')
    allergins = request.form.getlist('recipie_allergins')
    recipie_id = request.form.get('recipie_id')
    createdDate = request.form.get('createdDate')
    updatedDate = request.form.get('updated_date')
    likes = int(request.form.get('likes', 0))
    dislikes = int(request.form.get('dislikes', 0))
    difficulty = request.form.get('recipie_difficulty')
    mealtype = request.form.get('recipie_mealtype')
    toolsrequired = request.form.get('recipie_implements')
    currentimage = request.form.get('currentimage')
    # Check to see if there is a current image
    if currentimage is not None:
        # Then check to see if a new image has been passed through
        if 'recipie_image' in request.files:
            file = request.files['recipie_image']
            image = secure_filename(file.filename)
            print(os.path.join(app.config['BASE_PATH'], image))
            file.save(os.path.join(app.config['BASE_PATH'], image))
        elif currentimage is 'awaiting_image.png':
            image = 'awaiting_image.png'
        else:
            image = currentimage 
    # custom print to file for the tests
    def printtest(label, field, expectedtype):
        file.write(
                "Expecting type of {0}, for field {1}"
                .format(expectedtype, label) + '\n')
        file.write(str(isinstance(field, expectedtype)) + "\n")
        file.write("Test Passed \n")
        file.write("********* \n")
    # Automated Test - writes to testresults.txt
    file = open("testresults.txt", "a")
    file.write("*****Testing submission for " + title + "************\n")
    # Test followed by the print function
    is_expected_type('recipie_title', title, str)
    printtest('recipie_title', title, str)

    is_expected_type('recipie_description', description, str)
    printtest('recipie_description', description, str)

    is_expected_type('recipie_ingredients', ingredients, str)
    printtest('recipie_ingredients', ingredients, str)

    is_expected_type('recipie_allergins', allergins, list)
    printtest('recipie_allergins', allergins, list)

    # While the type is a bson.ObjectID,
    # it passes it through as a string value,
    # hence checking for a str
    if recipie_id is not None:
        is_expected_type('ObjectId', recipie_id, str)
        printtest('ObjectId', recipie_id, str)
    # Dates do not have their own type in python,
    # therefore we check for a string, which the datetime
    # library will convert for us
    is_expected_type('Created Date', createdDate, str)
    printtest('Created Date', createdDate, str)
    # Since new records do not contain an updated date, we need to skip this
    if updatedDate is not None:
        is_expected_type('Updated Date', updatedDate, str)
        printtest('Updated Date', updatedDate, str)

    is_expected_type('Likes', likes, int)
    printtest('Likes', likes, int)

    is_expected_type('Dislikes', dislikes, int)
    printtest('Dislikes', dislikes, int)

    is_expected_type('recipie_difficulty', difficulty, str)
    printtest('recipie_difficulty', difficulty, str)

    is_expected_type('recipie_mealtype', mealtype, str)
    printtest('recipie_mealtype', mealtype, str)

    is_expected_type('recipie_implements', toolsrequired, str)
    printtest('recipie_implements', toolsrequired, str)

    file.close()
    data = {
            "recipie_title": title, "recipie_description": description,
            "recipie_instructions": instructions,
            "recipie_ingredients": ingredients, "recipie_allergins": allergins,
            "createdDate": createdDate, "updatedDate": updatedDate,
            "recipie_difficulty": difficulty, "likes": likes,
            "dislikes": dislikes, "recipie_mealtype": mealtype,
            "recipie_implements": toolsrequired,
            "recipie_image": image
            }
    recipies = mongo.db.recipies
    if not recipie_id:
        flash('Recipie added', 'success')
        recipies.insert_one(data)
        return redirect('/results/')
    else:
        flash('Recipie updated', 'success')
        recipies.update({"_id": ObjectId(recipie_id)}, data)
        return redirect('/results/')


# Results page
@app.route('/results/')
def results():
    '''
    Results page
        @arg - page = The current page number
        @arg - sr = The start index for the results page,
        20 means that it will start at index 20
        @arg - qt = The query term
        @arg - allergin = The selected allergins from the filter to be excluded
    '''
    title = "Results | RecipieDB"
    filterOptions = []
    # Format is allergin => selected
    allerginlist = {
                    "Gluten": '0', "Crustacean": '0', "Eggs": '0',
                    "Fish": '0', "Peanuts": '0', "Soybeans": '0',
                    "Milk": '0', "Nuts": '0', "Celery": '0',
                    "Mustard": '0', "Sesame": '0', "Lupin": '0',
                    "Molluscs": '0'
                    }
    # Check to see if any parameters are defined
    if request.args.get('page'):
        page = int(request.args.get('page'))
        sr = int(request.args.get('sr'))
        currentpagenum = int(page)
    # If not, assign the default values
    else:
        page = 0
        sr = 0
        currentpagenum = 0
    results = []
    if request.args.get('qt'):
        query = request.args.get('qt')
        varlist = []
        # Check for allergin filter
        if request.args.get('allergin'):
            allergin = request.args.getlist('allergin')
            for aagin in allergin:
                varlist.append(aagin)
                newallergin = {aagin: '1'}
                allerginlist.update(newallergin)
            recipies = mongo.db.recipies.find(
                                            {"$text":
                                                {"$search": query},
                                                "recipie_allergins":
                                                {"$nin": varlist}})
            for r in recipies:
                results.append(r)
        else:
            recipies = mongo.db.recipies.find(
                                            {"$text":
                                                {"$search": query}})
            for r in recipies:
                results.append(r)
    else:
        query = ''
        varlist = []
        # Check for allergin filter
        if request.args.get('allergin'):
            allergin = request.args.getlist('allergin')
            for aagin in allergin:
                varlist.append(aagin)
                newallergin = {aagin: '1'}
                allerginlist.update(newallergin)
            recipies = mongo.db.recipies.find(
                                            {"recipie_allergins":
                                                {"$nin": varlist}})
            for r in recipies:
                results.append(r)

        else:
            recipies = mongo.db.recipies.find()
            for r in recipies:
                results.append(r)
    pagecount = 0
    # We set the number to 11, since it is 0 based indexing,
    # otherwise it only shows 9 results
    if len(results) < 11:
        pages = 0
    else:
        # Determine the number of result pages
        pages = int(len(results) / 11)
        if pages == 0:
            pagecount = pages
        else:
            pagecount = pages + 1
    return render_template(
                        'results.html', title=title,
                        currentQueryTerm=query,
                        allerginList=allerginlist,
                        selectedFilters=filterOptions,
                        results=results, c_page=currentpagenum,
                        pc=pagecount, pages=pages, sr=sr, nh=10,
                        maxresults=len(results))


@app.route('/recipie')
def recipie():
    '''
   Recipie page
        @arg - id = The ID of the recipie to be displayed
    '''
    def convertDate(field):
        '''
        This function takes a full datetime string
        and returns the date part ONLY
        '''
        year = field[0:4]
        month = field[5:7]
        day = field[8:10]
        date = day + "/" + month + "/" + year
        return date
    error = None
    if request.args.get('id'):
        record_id = request.args.get('id')
        rec = mongo.db.recipies.find_one({"_id": ObjectId(record_id)})
        if rec is None:
            flash('Record Not Found', 'error')
            return redirect('/')
        title = rec['recipie_title'] + " | RecipieDB"
        c_date = convertDate(rec['createdDate'])
        if rec['updatedDate'] is not None:
            u_date = convertDate(rec['updatedDate'])
        else:
            u_date = None

        return render_template(
                            'recipie.html', title=title,
                            recipie=rec, createdDate=c_date,
                            updatedDate=u_date)
    else:
        error = 'No recipie found'
        return render_template('index.html', error=error)


@app.route('/addLike', methods=['GET', 'POST'])
def addLike():
    '''
    Add Like Script (Called via AJAX)
    @arg - recordID = The record Id to add a like to
    '''
    record_id = request.args.get('recordID')
    recipies = mongo.db.recipies
    recipies.update({'_id': ObjectId(record_id)},
                    {'$inc': {'likes': int(1)}})
    return "Successfully added like"


@app.route('/addDislike', methods=['GET', 'POST'])
def addDislike():
    '''
    Add Dislike Script (Called via AJAX)
    @arg - recordID = The record Id to add a like to
    '''
    record_id = request.args.get('recordID')
    recipies = mongo.db.recipies
    recipies.update({'_id': ObjectId(record_id)},
                    {'$inc': {'dislikes': int(1)}})
    return "Successfully added dislike"


@app.route('/deleteRecipie')
def deleteRecipie():
    '''
    Script to delete a recipie
    '''
    record_id = request.args.get('id')
    if record_id is None:
        flash('Error deleting record, please try again', 'error')
        return redirect('/')
    recipies = mongo.db.recipies
    recipies.remove({'_id': ObjectId(record_id)})
    flash('Record successfully deleted', 'success')
    return redirect('/')


@app.route('/stats')
def stats():
    '''
    Statistics page
    This page initially writes to a
    json file the entire collection, it then calls the
    actual page to be rendered.

    The ObjectID is excluded from this json file.
    '''
    title = "Statistics | RecipieDB"
    client = MongoClient()
    collection = mongo.db.recipies
    cursor = collection.find({}, {"_id": 0})
    file = open("static/data/collection.json", "w")
    file.write('[')

    qnt_cursor = 0
    for document in cursor:
        qnt_cursor += 1
        num_max = cursor.count()
        if (num_max == 1):
            file.write(json.dumps(document))
        elif (num_max >= 1 and qnt_cursor <= num_max-1):
            file.write(json.dumps(document))
            file.write(',')
        elif (qnt_cursor == num_max):
            file.write(json.dumps(document))
    file.write(']')
    file.close()
    return render_template('stats.html', title=title)
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=False)
