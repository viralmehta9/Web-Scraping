# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 19:10:20 2016

@author: viral
"""

import urllib.request
from bs4 import BeautifulSoup

'''
os.getcwd()
os.chdir('D:\\MY ALL DESKTOP DATA\\Spring 2016\\Web and Social 5377\\InClassExercise')
f = csv.writer(open('OutputFile1.csv','w'))
'''

url = 'http://www.imdb.com/search/title?release_date=2014,2015&title_type=feature'

testUrl = urllib.request.urlopen(url)
readData = testUrl.read()
testUrl.close()

soup = BeautifulSoup(readData,'lxml')

# Using to track the no of movies
count = 0

# Fetchning the values present within the tags results
movies = soup.findChildren('table','results')

# Changing movies into an iterator
iterableMovies = iter(movies[0].findChildren('tr'))

# Skipping the first value of the iterator as it does not have the required data
next(iterableMovies)

# Finding the tr tag of iterableMovies. Every tr contains information of the movies.
for trItem in iterableMovies:
    
    #Fetching ImageURL for the movie
    imageURL = trItem.findChildren('td','image')[0].find('img')['src'].split('._V1.')[0] + '._V1_SX214_AL_.jpg'
    
    # fetching the title and year of movie
    movieTitle = trItem.findChildren('td','title')
    titleOFMovie = movieTitle[0].find('a').contents[0] + movieTitle[0].find('span','year_type').contents[0]
    movieDescription = movieTitle[0].find('span','outline').contents[0]
    # Fetching Genre
    genres = movieTitle[0].find('span','genre').find_all('a')
    genres = [g.contents[0] for g in genres]
    #Fetching movie time
    movieTime = movieTitle[0].find('span','runtime').contents[0]
    #Fetching Movie rating
    movieRating = movieTitle[0].find('span','value').contents[0]
    #------------ Printing resluts-------------
    count +=1
    print('Movie No: ' + str(count))
    print('Title: ' + titleOFMovie)
    print('Outline: ' + movieDescription)
    stringGenre = ''
    for item in genres:
        stringGenre += item + ', '
    print('Genres: ' + stringGenre)
    print('Movie Duration: ' + movieTime)
    print('Rating: ' + movieRating)
    print('\n\n')
    
    # To display 10 movies
    if count==10:
        break
    
    

