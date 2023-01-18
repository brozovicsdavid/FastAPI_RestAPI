from bs4 import BeautifulSoup
import requests
import re

list = []

def scrape():
     #scrape the data from the url
    url = 'http://www.imdb.com/chart/top'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    #create the values for the dictionary
    movies = soup.select('td.titleColumn')
    cast = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
    ratings = [b.attrs.get('data-value')
    for b in soup.select('td.posterColumn span[name=ir]')]

    for index in range(0, len(movies)):
        
        movie_string = movies[index].get_text() 
        movie = (' '.join(movie_string.split()).replace('.', ''))
        movie_title = movie[len(str(index))+1:-7]
        year = re.search('\((.*?)\)', movie_string).group(1)
        id = index + 1
        rating = round(float(ratings[index]),1) 
        dict = {'id':id,'movie_title':movie_title,'ratings':rating, 'year':year,'cast':cast[index]}
        list.append(dict)
        dict = {}
    
    return list