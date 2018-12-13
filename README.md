# **Indeed Web Scraping Application**

# **Introduction**
This application scrapes data from Indeed and displays the data on a webpage and stores it in a SQL database.
The application reads in a job description and list of cities from the user and returns results for jobs in 
each of the cities.

# **How to use**
Once the file is running a message similar to:  *"Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)"* 
will appear. This contains the URL that our web application is hosted in. 
Accessing the web application will take you to the home page where you can input the job description and
a list of cities you'd like to scrape data for. The cities must be separated by commas.

![Job Scraping Image](/Images/search_page.PNG)

The algorithm for scraping will take a while. The more cities entered, the longer the run time as there is a sleep
timer in between pages. Once the scraping has completed the user will be redirected to an output page that contains
a simple view of the data scraped and there will also be a SQL database created containing the data.

# **Files**
* **\_\_init\_\_.py**
	Main file that routes users to corresponding web pages and runs application functions
* **jobs.py**
	Contains functions for scraping data
* **files in template folder**
	Contains html files for each of the web pages
* **navbar.html (found in includes folder)**
	html file for the navigation bar

# **Packages Required**
I used the Anaconda platform for this project. I created my virtual environment to house my libraries and 
downloaded all the corresponding libraries in Anaconda. This platform is not required for this project and
the base Python can be used.

Documentation for creating virtual environments in Anaconda can be found here:
https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/
Documentation for creating virtual environments in base Python can be found here:
https://docs.python-guide.org/dev/virtualenvs/

libraries used for this application:
* BeautifulSoup: library for pulling data out of HTML and XML files
* Flask: web development framework
* html5lib: a pure-python library for parsing HTML
* Pandas: open source library with data analysis tools
* Sqlite3: a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language.
* Time: library that allows us to take breaks in between data scraping so the website doesn't boot 
us for scraping too much data

Run the following commands to install in virtual environment (Conda comes with the first 3 packages pre-installed)

`<$ pip install flask>`

`<$ pip install Beautifulsoup4>` 

`<$ pip install html5lib>`

`<$ pip install Pandas>`

`<$ pip install sqlite3>`

`<$ pip install Time>`

Once these files are downloaded you can proceed to run the \_\_init\_\_.py
