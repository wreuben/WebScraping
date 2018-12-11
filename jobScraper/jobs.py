import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

from time import sleep
import os #for clearing console
#clear = lambda:os.system('cls')
#clear()
import pandas as pd
import requests
import time #limit scraping 

os.chdir(r'C:\Users\rew.P3-GROUP.000\Documents\IE\IE 498\IE 498 Project\WebApplication2\JobScraper')
os.getcwd()

def get_title(div):
    try:
        return div.find("a",attrs={"data-tn-element":"jobTitle"}).text.strip()
    except:
        return 'None' 

def get_company(div):
    try:
        return div.find("span",attrs={"class":"company"}).text.strip()
    except:
        return 'None'

def get_location(div):
    try:
        return div.find("span",attrs={"class":"location"}).text.strip()
    except:
        return 'None'

def get_salary(div):
    try:
        return div.find(name="span",attrs={"class":"no-wrap"}).text.strip()
    except:
        return 'None'
def get_description(div):
    try:
        return div.find(name="span",attrs={"class":"summary"}).text.strip()
    except:
        return 'None'
title=[]

#Initializing empty dataframe
ID = []
company=[]
location=[]
salary=[]
description=[]

#for city in city_list: #NOTE: have to further add city into url

no_results = 300 #total number of results to return for each city
per_page = 50 #number of results to scrape per page for each city
job = "supply+chain+analyst"
cities = ["Austin","San+Francisco","Boston","Chicago","Los+Angeles","New+York","Washington"]

labels = ["ID","title","company","location","salary","description"] #dataframe column labels
df = pd.DataFrame(columns=labels) #dataframe initialization

for city in cities: #looping through predefined list of cities
        print('compiling results for: ',city)
        for page in range(0,no_results,per_page): #looping through each page in increments of per_page
            URL = "https://www.indeed.com/jobs?q={}&l={}&start={}&limit={}".format(job,city,page,per_page)
            page = requests.get(URL) #retrieve URL
            page_soup = soup(page.text,"html5lib") #parse URL

            counter = 1
            for div in page_soup.find_all("div",attrs={"class":"row"}): #for loop through all rows to extract results
                df = df.append({'ID':counter,'title':get_title(div),'company':get_company(div),'location':get_location(div),
                       'salary':get_salary(div),'description':get_description(div)},ignore_index=True) #update dataframe with job searches
                counter = counter + 1
            sleep(1) #sleeping one second between scrapes    
df[['title','company']]

#----------------------------
# SQLITE
#----------------------------
import sqlite3
conn = sqlite3.connect("jobs.db") #Create connection to SQLite database
c = conn.cursor() #define cursor object to perform SQL commands

c.execute('DROP TABLE IF EXISTS jobs;') #drop table
sql = """CREATE TABLE IF NOT EXISTS jobs (ID integer, title varchar(50),company varchar(50),location varchar(30),salary varchar(20),description text);""" 

c.execute(sql)
df.to_sql(name='jobs',con=conn,if_exists='append',index=False)

c.execute("select * from jobs")
conn.close #close connection
