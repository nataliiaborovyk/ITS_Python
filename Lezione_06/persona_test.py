#dal file persona.py importa la classe persona
from persona import Persona

#creare un ogetto di prima persona
nb:Persona = Persona("Nataliia", "Borovyk", 40)

print(nb)
print(nb.name, nb.lastname, nb.age)

from persona2 import Persona

nb:Persona = Persona()

#voglio richiamare la funzione displaydata di classe funzione per stampare in output le informazioni relative alla persona
nb.displayData()

#impostare il nome della persona nb
nb.setName("Nataliia")

print("")
nb.displayData()

#impostare il cognome 
nb.setLastname("Borovyk")

#impostare eta
nb.setAge(40)

print("")

nb.displayData()
print("")
print(nb.getName(),nb.getLastname(), nb.getAge())

#set imposta, get ritorna