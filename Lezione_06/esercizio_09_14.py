'''
Lottery: Create a class LotteryMachine that holds a list containing a series of 10 numbers and 5 letters. 
Implement a method to randomly select 4 items (numbers or letters) from this list to draw a winning ticket. 
Finally, implement a method to display a message saying that any ticket matching the winning 4 items wins a prize.
'''
import random


class LotteryMachine:

    def __init__(self, lista:list = None, ticket:list = None):
        if lista == None:
            self.lista = [1,2,3,4,5,6,7,8,9,0,"m","a","k","t"]
        else:
            self.lista = lista
        if ticket == None:
            self.ticket = []
        else:
            self.ticket = ticket

    def winningTicket(self):
        self.ticket = random.choices(self.lista, k=4)      #random.choices() permette di sceliere dalla lista quantita di caratteri richiesti con possibili ripetizioni
                                                           #random.sample() permette di sceliere dalla lista quantita di caratteri richiesti SENZA ripetizioni
    def infoTicket(self):
        print(f"Ticket matching {self.ticket} wins a prize")

tick_1:LotteryMachine = LotteryMachine()
tick_1.winningTicket()
tick_1.infoTicket()