
#from imdb_api import IMDb
from imdb_api import IMDb

movie = IMDb().getTitle('1')
print(movie)
m=IMDb().getDirector('1')
print(m)

