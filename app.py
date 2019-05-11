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

@app.route('/results/')
def results():
    '''
    Performs the actual pagination
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
    resultnum = ['Joseph Allen', 'Autumn Welch', 'Valerie Fields', 'Margaret Mccarty', 'Patricia Yu', 'Kelsey Burton', 'Charles Chandler', 'Michelle Washington', 'Wendy Morris', 'Sherri Perez', 'Holly Campbell', 'Karen Cisneros MD', 'Jessica Perry', 'Kimberly Miranda', 'Michael Lawrence']
    
    
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