from compito_21 import MovieCatalog

#inizializamo un catalogo, ovego ogetto della classe catalog

catalog: MovieCatalog = MovieCatalog()
#print(catalog)
catalog.add_movies("Spielberg", ["Casper", "Ritorno al futuro"])
#print(catalog)
catalog.add_movies("Spielberg", ["ET"])
#print(catalog)
catalog.add_movies("Quentin Tarantino", ["Pulp", "Kill Bill"])
#print(catalog)
catalog.remove_movie("Quentin Tarantino", "Kill Bill")
#print(catalog)
catalog.remove_movie("Quentin Tarantino", "Pulp")
#print(catalog)
print(catalog.list_directors())
print(catalog.get_movies_by_director("Tim Barton"))
print(catalog.get_movies_by_director("Spielberg"))