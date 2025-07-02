'''
8-8. User Albums: Start with your program from Exercise 8-7. 
Write a while loop that allows users to enter an album’s artist and title. 
Once you have that information, call make_album() with the user’s input 
and print the dictionary that’s created. Be sure to include a quit value in the while loop.
'''

print("\n   Esercizio 8-8")

#function that builds a dictionary describing a music album
def make_album(name:str, title:str, songs:int = None) -> dict[str, str, int]: 
        return {"Artist": name, "Album": title, "Songs": songs}

#utente inserice nome del artista e dell'album e se vuole anche quantita di cansoni
while True:
        scelta:str = input("\nVuoi inserire informazioni? Risposta si o no: ")
        match scelta:
             
            case "si":
                 x:str = input("\nInserisci il nome del artista: ")
                 y:str = input("\nInserisci il nome del album: ")
                 z:str = input("\nVuoi inserire il numero delle cansoni? Risposta si o no: ")

                 #verifico se uente desidera inserire la quantita di cansoni
                 match z:
                      
                    case "si":
                        z:int = int(input("\nIserire il numero delle cansoni: "))
                        diz: dict[str, str, int] = make_album(x, y, z)
                        print("")
                        for k,v in diz.items():
                            print(f" {k}: {v}")

                    case "no":
                        diz: dict[str, str] = make_album(x, y)
                        print("")
                        for k,v in diz.items():
                            print(f" {k}: {v}")
            case "no":
                  break
                          
                    
