'''
Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, 
cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.
print(check_parentheses("()()"))   Result  True
print(check_parentheses("(()))("))         False
'''

#VERSIONE 1        

def check_parentheses(expression: str) -> bool:

    cont:int = 0
    for i in range(len(expression)):
        if expression[i]  == "(":
            cont -= 1
        elif expression[i]  == ")":
            cont += 1
    if cont == 0 and expression[0] == "(" and expression[-1] == ")":
        return True
    else:
        return False
    
print(check_parentheses("()()"))       #True
print(check_parentheses("(()))("))     #False
print(check_parentheses("((())))"))     #True
print(check_parentheses(")("))         #False
print(check_parentheses("(())"))       #True



#VERSIONE 2

def check_parentheses(expression: str) -> bool:

    cont:int = 0
    for i in range(len(expression)):
        if expression[i]  == "(":
            cont += 1
        elif expression[i]  == ")":
            if cont >= 1:
                cont -= 1
            else:
                return False
            
    if cont == 0:
        return True
    else:
        return False

print("")
print(check_parentheses("()()"))       #True
print(check_parentheses("(()))("))     #False
print(check_parentheses("((()))"))     #True
print(check_parentheses(")("))         #False
print(check_parentheses("(())"))       #True