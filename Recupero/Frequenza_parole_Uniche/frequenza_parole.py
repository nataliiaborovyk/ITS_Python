import re

def FrequenzaParole(testo:str) -> dict[str,int]:
    result:list[str] = re.findall(r'\b\w+\b', testo.lower())
    output: dict[str, int] = {}
    for i in result:
        if i not in output:
            output[i] = 1
        else:
            output[i] += 1
    return output
        
if __name__ == "__main__":
    testo1:str = ("Hello, world! Hello... PYTHON? world.")
    print(FrequenzaParole(testo1))

