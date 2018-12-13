#------------------------------------------------
###IMPORTING LIBRARIES AND CLASSES###
#------------------------------------------------
import bs4
from bs4 import BeautifulSoup as soup

from time import sleep
import os #for clearing console
#clear = lambda:os.system('cls')
#clear()
import pandas as pd
import requests
import time #limit scraping 

#-----------------------------------------------------------------------------------
###Functions to scrape individual components of jobs from indeed html layout###
#-----------------------------------------------------------------------------------
def get_title(div): #Function to scrape job title of jobs on Indeed pages
    try:
        return div.find("a",attrs={"data-tn-element":"jobTitle"}).text.strip()
    except:
        return 'None' 

def get_company(div): #Function to scrape company name of jobs on Indeed pages
    try:
        return div.find("span",attrs={"class":"company"}).text.strip()
    except:
        return 'None'

def get_location(div): #Function to scrape location of jobs on Indeed pages
    try:
        return div.find("span",attrs={"class":"location"}).text.strip()
    except:
        return 'None'

def get_salary(div): #Function to scrape salary of jobs on Indeed pages
    try:
        return div.find(name="span",attrs={"class":"no-wrap"}).text.strip()
    except:
        return 'None'
def get_description(div): #Function to scrape job descriptions of jobs on Indeed pages
    try:
        return div.find(name="span",attrs={"class":"summary"}).text.strip()
    except:
        return 'None'
title=[]

###TEST INPUT TO TEST FUNCTION job_search###
job = "project+manager" 
cities = ["Austin","San+Francisco","Boston","Chicago","Los+Angeles","New+York","Washington"]

#--------------------------------------------------------------------------------------
###Main Function that calls all scraping functions and appends to dataframe###
#1. Initializes an empty dataframe to store all the job descriptions
#2. Runs a for loop through all the cities as specified by the user
#3. Within each city there is another for loop through that calls the previously
#   defined functions and extracts ID, title, company, location, salary and description
#   and then appends it to the dataframe
#4. Function then returns dataframe.
#--------------------------------------------------------------------------------------
def job_search(job, cities): 
    no_results = 100 #total number of results to return for each city
    per_page = 50 #number of results to scrape per page for each city

    labels = ["ID","title","company","location","salary","description"] #dataframe column labels
    df = pd.DataFrame(columns=labels) #dataframe initialization
    for city in cities: #looping through predefined list of cities
            print('compiling results for: ',city)
            for page in range(0,no_results,per_page): #looping through each page in increments of per_page
                URL = "https://www.indeed.com/jobs?q={}&l={}&start={}&limit={}".format(job,city,page,per_page) #custom URL with user inputs
                page = requests.get(URL) #retrieve URL
                page_soup = soup(page.text,"html5lib") #parse URL

                counter = 1
                for div in page_soup.find_all("div",attrs={"class":"row"}): #for loop through all rows to extract results
                    df = df.append({'ID':counter,'title':get_title(div),'company':get_company(div),'location':get_location(div),
                           'salary':get_salary(div),'description':get_description(div)},ignore_index=True) #update dataframe with job searches
                    counter = counter + 1
                sleep(1) #sleeping one second between scrapes
    return df #return dataframe


