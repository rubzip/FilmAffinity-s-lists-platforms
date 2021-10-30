from bs4 import BeautifulSoup
import pandas as pd
import requests


#Takes a movie as a soup object and returns: (name, rating, link) of the movie
def movie_info(movie):
    head = movie.find('div', class_='mc-title')
    name = head.find('a')['title']   
    link = head.find('a')['href']
    rating = movie.find('div', class_='avgrat-box').text 
    
    return(name, rating, link)


#Takes the movie's FA page as a soup object and returns all platforms where it's possible to watch this movie by subscription
def rent_plattforms(soup):
    info  = soup.find('div', class_='film-right-box vod-wrapper')
    if(info is not None):
        info  = info.find_all('div', class_='prov-offers-wrapper big-offers')
        index = soup.find('div', class_='film-right-box vod-wrapper').find_all('div', class_='sub-title')
        platfforms = []
        for i in range(len(index)):
            if(index[i].text == 'Suscripción'):
                aux = info[i].find_all('img')
                for platfform in aux:
                    platfforms.append( platfform['alt'] )
    
        return(platfforms)
    else:
        return([])

#Takes a list of lists and returns a  DataFrame
def generate_movies_df(data):
    colunms = ['Name', 'Rating', 'Platforms', 'URL']
    df = pd.DataFrame(data, columns=colunms)
    
    return(df)


#Takes the DataFrame of all movies in your list and all your platforms and returns a  DF of all movies you can watch 
def what_you_can_watch(df, your_plattforms):
    you_can_watch_list = []
    
    for i in df.index:
        platforms = df.loc[i, 'Platforms']
        you_can_watch = False
        for platform in your_plattforms:
            you_can_watch = you_can_watch or (platform in platforms)
        if(you_can_watch):
            you_can_watch_list.append( list(df.loc[i, :]) )
            
    df = generate_movies_df(you_can_watch_list)
    return(df)


#Takes the URL of the FA's list and returns a list of all movies in the list as soup objects
def import_movies(URL, num_pages=10):
    URL_page = URL + '&page={}'
    pages = []
    for i in range(num_pages):
        page = requests.get(URL_page.format(i+1))
        soup = BeautifulSoup(page.content, 'html')
        pages.append(soup)
    #Makes a list of all movies in the list (as a soup object)
    movies = []
    for soup in pages:
        movies += soup.find_all('div', class_='mc-info-container')
    return(movies)