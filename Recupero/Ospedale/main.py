from persona import Persona
from paziente import Paziente
from dottore import Dottore
from fatture import Fattura

dot1: Dottore = Dottore("Alex", "Pippo", "Psichiatra", 5000.0)
dot2: Dottore = Dottore("Anna", "Bella", "Veterinaria", 3006.0)

dot1.setAge(50)
dot2.setAge(31)

paz1: Paziente = Paziente("Bilbo", "Begins", "asd12")
paz1.setAge(95)

paz2: Paziente = Paziente("King", "Kong", "afn23")
paz2.setAge(157)

paz3: Paziente = Paziente("Merlin", "Grigio", "kkk111")
paz3.setAge(468)

paz4: Paziente = Paziente("Frodo", "Begins", "jjj3")
paz4.setAge(40)

paz5: Paziente = Paziente("Bella", "Principessa", "sjd5")
paz5.setAge(18)

lista1: list[Paziente] = [paz1, paz3, paz4]
lista2: list[Paziente] = [paz2, paz5]

dot1.greet()
dot2.greet()

fattura1: Fattura = Fattura(dot1, lista1)
fattura2: Fattura = Fattura(dot2, lista2)

print(f"Salario Dottore1: {fattura1.getSalary()} euro")
print(f"Salario Dottore2: {fattura2.getSalary()} euro")


fattura1.removePatient("asd12")
fattura2.addPatient(paz1)

print(f"Salario Dottore1: {fattura1.getSalary()} euro")
print(f"Salario Dottore2: {fattura2.getSalary()} euro")

salary_osp:int = fattura1.getSalary() + fattura2.getSalary()
print(f"In totale l'ospedale ha incassato {salary_osp}")