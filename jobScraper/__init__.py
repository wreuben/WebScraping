#------------------------------------------------
###IMPORTING LIBRARIES AND CLASSES###
#------------------------------------------------
from flask import Flask, request, render_template #import flask class to begin web development
import pandas as pd #import pandas to deal with dataframes
import jobs #call and import jobs.py file
import sqlite3

#-----------------------------------------------------------------------------------
###FLASK APPLICATION###
#1. Multiple functions for routing users to corresponding URLs
#2. The design and layout of each of these URLs can be found in the
#   JobScraper/templates folder
#3. Flask application runs function my_form_post() when user inputs the 
#   search criteria.
#4. The function calls the job scraping function from jobs.py and outputs
#   the dataframe as well as stores it into a SQL database
#-----------------------------------------------------------------------------------
app = Flask(__name__) #create instance of flask class

@app.route('/') #route() decorator to tell Flask what URL should trigger our function
def index():
    return render_template('home.html') #return home page

@app.route('/', methods=['POST']) #route() for our search box
def my_form_post(): #processing text from search box
    text1 = request.form['job'] #get user input text for job
    text2 = request.form['cities'] #get user input for cities to search through

    words = text1.split() #split up user text into a list for processing
    cities = text2.replace(" ","").split(",") #split up cities into list for processing

    search = "" #initialize empty string that will contain the job description to search
    for word in words: #for loop to make job description format fit into indeed url
        search = search + word + "+" 
    print("we are searching for the job description: ",text1, " in the following cities: ",text2) 

    data = jobs.job_search(search,cities)

    #-----------------------------------
    # Putting data into sqlite database
    #-----------------------------------
    conn = sqlite3.connect("jobs.db") #Create connection to SQLite database
    c = conn.cursor() #define cursor object to perform SQL commands

    c.execute('DROP TABLE IF EXISTS jobs;') #drop table
    sql = """CREATE TABLE IF NOT EXISTS jobs (ID integer, title varchar(50),company varchar(50),location varchar(30),salary varchar(20),description text);""" 

    c.execute(sql)
    data.to_sql(name='jobs',con=conn,if_exists='append',index=False)

    conn.close #close connection
    return render_template('data.html',data=data.to_html()) #return data page

@app.route('/about') #route for the about page
def about():
    return render_template('about.html') #return about page

@app.route('/contact') #route for the contact page
def contact():
    return render_template('contact.html') #return contact page

if __name__ == '__main__':
    app.run(debug=False)