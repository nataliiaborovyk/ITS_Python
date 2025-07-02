
from film import Film
from sala import Sala
from cinema import Cinema

print("\n     Class Film")

f1: Film = Film()
print(f"\ntest: {f1}")
f1.setTitolo("Alice al mare")
f1.setDurata(90)
print(f"Atributi aggiornati: {f1}")

f2: Film = Film()
f2.setTitolo("Alice in montagna")
f2.setDurata(60)
print(f"Atributi aggiornati: {f2}")


print("\n    Class Sala")

s1=Sala()
print(f"\ntest: {s1}")
s1.setNumId(1)
s1.setNumId(-3)
s1.setFilmAttuale(f1)
s1.setPostiTot(50)
print(f"Atributi aggiornati: {s1}")
print(f"Posti disponibili: {s1.posti_disponibili()}")
print(s1.prenota_posti(24))
print(f"Posti disponibili: {s1.posti_disponibili()}")
print(f"Provo a prenotare 30 posti\n" , s1.prenota_posti(30))

s2=Sala()
print(f"\ntest: {s2}")
s2.setNumId(2)
s2.setFilmAttuale(f2)
s2.setPostiTot(20)
print(f"\Atributi aggiornati: {s2}")
print(s2.prenota_posti(5))
print(f"Posti disponibili: {s2.posti_disponibili()}")
print(f"Provo a prenotare 32 posti")
print(s2.prenota_posti(32))


print("\n    Class Cinema")

c1:Cinema = Cinema()
c1.aggiungi_sala(s1, s2)
c1.menu_film()
print(f"\nPosti disponibili: {s1.posti_disponibili()}")
c1.prenota_film("alice al mare", 5)
print(f"Posti disponibili: {s1.posti_disponibili()}")
print("Provo prenotare 60 posti")
c1.prenota_film("alice al mare", 60)
print("Provo prenotare -2 posti")
c1.prenota_film("alice al mare", -2)
c1.prenota_film("Alice e Marco", 60)    