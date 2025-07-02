'''
Scrivi una funzione che converte una temperatura da gradi Celsius a Fahrenheit e viceversa a seconda del parametro to_fahrenheit. Utilizza il concetto di parametri opzionali per il parametro to_fahrenheit.
print(convert_temperature(0))          Result  32.0
print(convert_temperature(32, False))          0.0
'''

def convert_temperature(temp:float, to_fahrenheit:bool = True) -> float:

    if to_fahrenheit  == False:
        gradi_celsius = (temp - 32) / 1.8
        return gradi_celsius
    else: 
        gradi_fahrenheit = temp * 1.8 + 32
        return gradi_fahrenheit
    
print(convert_temperature(0))            #32.0
print(convert_temperature(32, False))    #0.0
print(convert_temperature(100))          #212.0
print(convert_temperature(212, False))   #100.0
print(convert_temperature(-40))          #-40.0