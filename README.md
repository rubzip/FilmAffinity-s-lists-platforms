# FilmAffinity's lists platforms

FA does't show in what platforms you can watch movies from a FA's list.

I have made my own solution using webscrapping.

## VPNs and Platforms

Platforms catalogue is different in every country, there are some movies that you can see in Netflix US but not in Netflix UK.

I have automatized the way to search. The program gives you in what platforms you can watch the movies in four countries: Spain, US, UK and Canada (I'm limited by FilmAffinity). So if you have access to a VPN, you can watch more movies!

## Prerequisites

```
  python 3.X
  BeautifulSoup4
  pandas
  jupyter-notebook (optional)
```

## Scripts

The program can be run indifferently as as a python script (`main.py`) or a jupyer notebook (`what_you_can_watch_from_a_FilmAffinity_list.ipynb`).

 * `main.py` : Main script.
 * `what_you_can_watch_from_a_FilmAffinity_list.ipynb` : Main script as a jupyter notebook
 * `fun.py` : Contains all functions.

## Acepted platforms and countries

```python
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
 'HBO Max'
 ]
#All countries:
all_countries = [
 'es', #Spain
 'us', #US
 'uk', #UK
 'ca', #Canada
]
```

## Input

The input of the script goes here:
```python
#Only edit this cell:

#URL of the list:
URL = 'https://www.filmaffinity.com/es/userlist.php?user_id=9046485&list_id=1005'
#Number of pages of the list:
num_pages = 6
#Folder where CSVs are contained:
folder_name = './lists/'
#List name:
list_name = 'PELIS Q VER OBL'
#Name of the CSV generated with all movies in FA's list
CSV_file_name = list_name + '_list.csv'
#Name of the CSV generated with all movies in FA's list that you can watch
CSV_file_you_can_watch = list_name +  '_you_can_watch.csv'
#List of all platforms where you have an account:
your_plattforms = ['Amazon Prime Video', 'Filmin']
#Countries (VPN): 
countries = ['es']
```
To obtain the URL you have to click share on the FA's list and copy the link.
![URL](https://github.com/rubzip/FilmAffinity-s-lists/blob/main/URL.jpg)

## Output

The output of the program consist on two .CSV files, a first one called `CSV_file_name`, a list of all movies from the list and in what platforms you can watch them. The second file `CSV_file_you_can_watch` collects all movies frome the list tha you can watch on your platforms.

# Listas de FilmAffinity

En FilmAffinity no puedes saber de manera directa en qué plataforma se encuentran las peliculas de una lista.

He implementado mediante webscrapping una solución a este problema.

## VPNs y plataformas

Por motivos de distribuidoras y derechos, el catálogo de las plataformas es distinto en cada país, existen algunas películas que pueden verse en Netflix US pero no en Netflix España.

Por esto he implementado una manera de automatizar la búsqueda. El programa te dice en qué plataformas puedes ver las películas de la lista en cuatro países: España, EEUU, Reino Unido y Canadá (el programa está limitado por FA). ¡Así que si tienes acceso a una VPN podrás ver muchas más peliculas!
