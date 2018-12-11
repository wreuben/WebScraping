from flask import Flask, render_template
import pandas as pd

#Test to call other python script
#from jobScraper import Hello
#Hello.hello()

from jobScraper import jobs
web_data = jobs.df

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/data')
def data():
    return render_template('data.html',data=web_data.to_html())

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=False)


