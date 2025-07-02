class Alieno:

    #inizializzare progetto di classe alieno
    def __init__(self, galaxy:str):
        self.setGalaxy(galaxy)

    def setGalaxy(self, galaxy:str) -> None:
        if galaxy:
            self.galaxy = galaxy
        else:
            print("la galassia di provenienza non puo essere la stringa vuota")

    def getGalaxy(self) -> str:
        return self.galaxy
    
    def speak(self) -> None:
        print("kjhgdkghergkhdslgkjh")

    def __str__(self) -> str:
        return f"\nAlieno proveniente dalla galassia {self.getGalaxy()}"