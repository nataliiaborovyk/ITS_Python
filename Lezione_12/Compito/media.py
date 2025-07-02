class Media:
    def __init__(self, title:str, year:int) -> None:
        self.setTitle(title)
        self.setYear(year)

    def setTitle(self, title:str) -> None:
        if title:
            self.title = title
        else:
            print("Error")
    
    def setYear(self, year:int) -> None:
        if year:
            self.year = year
        else:
            print("Error")

    def getTitle(self) -> str:
        return self.title
    
    def getYear(self) -> str:
        return self.year

    def __str__(self) -> str:
        return f"Titolo: {self.getTitle()}\n Anno: {self.getYear}"
    
    