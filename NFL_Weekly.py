# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 01:35:34 2016

@author: viral
"""

import urllib

from bs4 import BeautifulSoup

import csv
import os


#path and output data file
os.getcwd()
directoryPath = "..\.."
os.chdir(directoryPath)
f = csv.writer(open("NFL_Weekly.csv","w"))
f.writerow(['Team Rank','Team Name','Team Points','Team Comments'])
url = 'http://espn.go.com/college-football/powerrankings'

testUrl = urllib.request.urlopen(url)
readData = testUrl.read()
testUrl.close()

soup = BeautifulSoup(readData,'lxml')
# Using to track the no of movies
count = 0
# Fetchning the values present within the tags results
teams = soup.findChildren('table','tablehead')

# Changing movies into an iterator
iterableTeams = iter(teams[0].findAll('tr'))

# Skipping the first value of the iterator as it does not have the required data
next(iterableTeams)
next(iterableTeams)

# to count 
n=0
# Finding the tr tag of iterableMovies. Every tr contains information of the movies.
for trItem in iterableTeams:
    
    n += 1
    #print(trItem)
    
    teamRank = trItem.findChildren('td','pr-rank')[0].get_text()
    #print(teamRank)
    teamName = trItem.findAll('a')[1].contents[0]
    #print(teamName)
    #teamRecord = trItem.find('span','pr-record').contents[0]
    #print(teamRecord)
    teamPoints = trItem.findChildren('td')[3].contents[0]
    #print(teamPoints)
    teamComments = trItem.findChildren('td')[4].contents[0]
    #print(teamComments)
    f.writerow([teamRank,teamName,teamPoints,teamComments])
    if n==25:
        break


    
    
    
   
