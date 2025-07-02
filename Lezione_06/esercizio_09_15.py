'''
Lottery Analysis: Extend the LotteryMachine class you created in Exercise 9-14.
1. Add a method called simulate_until_win(self, my_ticket) that:
    Accepts a ticket (a list of 4 items).
    Repeatedly draws random tickets using the draw_ticket() method.
    Keeps count of how many attempts it takes until a randomly drawn ticket matches my_ticket.
    Returns the number of attempts and the winning ticket.
2. Create a ticket called my_ticket with 4 numbers or letters from the pool.
3. Use the simulate_until_win() method to simulate how many draws it would take for your ticket to win.
4. Print a message showing:
    Your ticket
    The winning ticket
    How many attempts it took to win
'''

import random


class LotteryMachine:

    def __init__(self, lista:list = None, ticket:list = None):
        if lista == None:
            self.lista = [1,2,3,4,5,6,7,8,9,0,"a","b","c","d"]
        else:
            self.lista = lista
        if ticket == None:
            self.ticket = []
        else:
            self.ticket = ticket


    def winningTicket(self):
        self.ticket = random.choices(self.lista, k=4)

    def infoTicket(self):
        print(f"Ticket matching {self.ticket} wins a prize")

    def simulate_until_win(self, my_ticket:list):
        cont:int = 0
        while my_ticket != self.ticket:
            self.ticket = random.choices(self.lista, k=4)
            cont += 1
        print(f"You try {cont} times to win")

tick_1:LotteryMachine = LotteryMachine()
tick_1.winningTicket()
tick_1.infoTicket()
tick_1.simulate_until_win([1,2,"a","b"])

