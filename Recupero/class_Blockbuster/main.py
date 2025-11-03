from film import Film
from movie_genre import Azione, Dramma, Commedia
from noleggio import Noleggio

fa1: Azione = Azione(111, "Ciao Mare")
fa2: Azione = Azione(222, "Vivo felive")
fa3: Azione = Azione(333, "Bella ciao")
fa4: Azione = Azione(444, "Ciao Mondo")
fa5: Azione = Azione(555, "Amore")

fc1: Commedia = Commedia(666, "Mare")
fc2: Commedia = Commedia(777, "AMici")
fc3: Commedia = Commedia(888, "Nemici")
fc4: Commedia = Commedia(999, "Mondo")

fd1: Dramma = Dramma(1110, "GLobo") 

lista1: list[Azione | Dramma | Commedia]

n1: Noleggio = Noleggio([fa1,fa2,fa3,fa4,fa5,fc1,fc2,fc3,fc4,fd1])

print("Quale film vuoi nolleggiare")

n1.isAvaible(fa1)

n1.rentAMovie(fa1, 12)

n1.rentAMovie(fa2, 12)

n1.rentAMovie(fa1, 11)

n1.rentAMovie(fa3, 11)

n1.giveBack(fa2, 12, 4)

n1.printMovies()
