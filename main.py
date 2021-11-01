from bs4 import BeautifulSoup
import pandas as pd
import requests
from fun import *

#All acepted platforms:
all_platforms = [
 'Starz Play Amazon Channel',
 'Filmin Plus',
 'Movistar Plus',
 'Netflix',
 'Filmin',
 'fuboTV',
 'Rakuten TV',
 'HBO',
 'Microsoft Store',
 'Amazon Prime Video',
 'Spamflix',
 'Google Play Movies',
 'Amazon Video',
 'Apple iTunes',
 'HBO Max']
 
#All countries:
all_countries = [
 'es',
 'us',
 'uk',
 'ca',
 'ar',
 'mx'
]

#Only edit this cell:

#URL of the list:
URL = 'https://www.filmaffinity.com/es/userlist.php?user_id=9046485&list_id=220'
#Number of pages of the list:
num_pages = 2 
#Name of the CSV generated with all movies in FA's list
CSV_file_name = 'list.csv'
#Name of the CSV generated with all movies in FA's list that you can watch
CSV_file_you_can_watch = 'you_can_watch.csv'
#List of all platforms where you have an account:
your_plattforms = ['Filmin', 'Netflix']
#Countries (VPN): 
countries = ['es', 'us']

#Now we import all needed info from internet:
list_name, movies = import_movies(URL, num_pages)
data = []
print('Importing info from internet...')
for movie in movies:
    name, rating, URL = movie_info(movie)
    print('\t', name)
    
    platforms_countries = []
    for country in countries:
        page = requests.get(URL[:29]+country+URL[31:])
        soup = BeautifulSoup(page.content, 'html')
        platfforms = rent_plattforms(soup, country)
        platforms_countries.append(platfforms)
    
    data.append([name, rating] + platforms_countries + [URL])

#df stores all movies from the list as a DataFrame:
df = generate_movies_df(data, countries)
df.to_csv(CSV_file_name)

#df_you_can stores all movies that you can see as a Dataframe:
df_you_can = what_you_can_watch(df, your_plattforms, countries)
df_you_can.to_csv(CSV_file_you_can_watch)
print('You can watch from {} list all these movies: '.format(list_name))
print(df_you_can)
