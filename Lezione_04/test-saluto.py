
#inport saluto importa tutto il modulo saluto

import saluto
saluto.greet("Nat")


import saluto as s
s.greet("Nat")


#se voglio importare solo la funzione dal modulo saluto e ignorare il resto

from saluto import greet
greet("Nat")


from saluto import greet as g
g("Nat")