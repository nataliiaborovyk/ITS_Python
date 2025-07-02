

'''
Database of dates:  Write a class that manages a database of dates with the format gg.mm.aaaa implementing methods to add a new date,
 delete a given date, modify a date, and perform a query on a given date is required.  
 A query on a given date allows for retrieving a given new date. 
 Note that a date is an object for your database; it must be instantiated from a string.
'''

from datetime import datetime

class Data:

    def __init__(self, date:str = None):
        if date:
            try:
                self.date = datetime.strptime(date, '%d.%m.%Y')         #strptime method serve per convertire stringa in datetime object
            except ValueError:
                raise ValueError(f"{date} is not correct format, must be dd.mm.aaaa")
        else:
            self.date = None

         
    def __str__(self) -> str:
        if self.date:
            return f"Data: {self.date.strftime('%d.%m.%Y')}"        #strftime method serve per convertire datetime object in stringa
        else:
            return "Data does not exist yet"
        
   
    def setData(self, date:str):
        try: self.date = datetime.strptime(date, "%d.%m.%Y")       #strptime method serve per convertire stringa in datetime object
        except ValueError:
            raise ValueError(f"{date} is not correct format, must be dd.mm.aaaa")
        

    def getData(self):
        if self.date:
            return self.date.strftime("%d.%m.%Y")     #strftime method serve per convertire datetime object in stringa
        else:
            return "Data does not exist yet"



try:  
    date_1 = Data("132.32.4325")
    print(date_1)
except ValueError as error:
    print(error)

try:  
    date_2 = Data("08.04.2025")
    print(date_2)
except ValueError as error:
    print(error)



class Database:

    def __init__(self):
        self.listaData = []

    def __str__(self):
        return f"{self.listaData}"

    def setData(self, date:Data):
        #self.data = data
        self.listaData.append(date)

    def delData(self, date:Data):
        #self.date = date
        self.listaData.remove(date)

    def modifData(self, date:Data, dateNew:Data):
        self.date = date
        self.dateNew = dateNew
        for i in range(len(self.listaData)):
            if self.listaData[i] == self.date:
                self.listaData[i] = self.dateNew
            else:
                print(f"Error! Data {date} not in Datebase and can't be modify")

    def queryDate(self, date:Data):
        self.date = date
        for i in range(len(self.listaData)):
            if self.listaData[i] == self.date:
                print(f"Data {self.date} is in Datebase")
            else:
                print(f"Error! Data {date} not in Datebase")
               


birthday_database:Database = Database()
birthday_database.setData(date_2)
print(birthday_database)