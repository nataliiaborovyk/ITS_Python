from persona import Persona
from alieno import Alieno


#creare un oggetto p della classe persona
p: Persona = Persona("Nataliia", "Borovyk", 20)

#visualizare le informazioni relative alla persona p
print(p)

#creare un oggetto et della classe alieno
et: Alieno = Alieno("Andromeda")

#visualizare info relative a Alieno
print(et)

#oggetto p invoca il metodo speak
p.speak()

#oggetto et invoca il metodo speak
et.speak()
