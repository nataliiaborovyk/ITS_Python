import math

def ghipotenusa(a,b):
    return math.sqrt(a**2 + b**2)

if __name__ == "__main__":
    x = 4
    y = 3
    print(f"Nel tiangolo se \ncateto 1: {x} \ncateto 2: {y} \nghipotenusa = {ghipotenusa(x,y)}")