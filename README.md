# FilmAffinity's lists

FA does't show in what platforms you can watch movies from a FA's list.

I have made my own solution using webscrapping.

## VPNs and Platforms

Platforms catalogue is different in every country, there are some movies that you can see in Netflix US but not in Netflix UK.

I have automatized the way to search. The program gives you in what platforms you can watch the movies in four countries: Spain, US, UK and Canada (I'm limited by FilmAffinity). So if you have access to a VPN, you can watch more movies!

## Prerequisits

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

## Input

The input of the script goes here:
```python
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
```
To obtain the URL you have to click share on the FA's list and copy the link.

## Output



# Listas de FilmAffinity

En FilmAffinity no puedes saber de manera directa en qué plataforma se encuentran las peliculas de una lista.

He implementado mediante webscrapping una solución a este problema.

## VPNs y plataformas

Por motivos de distribuidoras y derechos, el catálogo de las plataformas es distinto en cada país, existen algunas películas que pueden verse en Netflix US pero no en Netflix España.

Por esto he implementado una manera de automatizar la búsqueda. El programa te dice en qué plataformas puedes ver las películas de la lista en cuatro países: España, EEUU, Reino Unido y Canadá (el programa está limitado por FA). ¡Así que si tienes acceso a una VPN podrás ver muchas más peliculas!
