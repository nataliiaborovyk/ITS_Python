'''
5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 
into an if-elif-else chain.
• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed 
for the appropriate color alien.
'''


#esercizio 5-5
print("\n Esercizio 5-5 \n")

alien_color: str = input("Di che colore è l'alieno? ").lower()

if alien_color == "green":
    print("Hai guadagnato 5 punti!")

elif alien_color == "yellow":
    print("Hai guadagnato 10 punti!")

else:
    alien_color == "red"
    print("Hai guadagnato 15 punti!")

