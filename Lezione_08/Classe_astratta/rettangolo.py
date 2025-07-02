from forma_generica import FormaGenerica

class Rettangolo(FormaGenerica):

    def __init__(self):
        super().__init__()

        self.setShape('rettangolo')

    def draw(self) -> None:
        print(f"\n{self.getShape()}\n")
        
        #outer for
        for i in range(5):
            #inner for
            for j in range(5*2):
                #formule per disegnare lato a e b
                if i == 0 or i == 5 - 1:
                    print("*", end=" ")
                #lato b e lato c
                elif j == 0 or j == 5*2 - 1:
                    print("*", end=" ")
                #stampare spazzi bianchi
                else:
                    print(" ", end=" ")
            print("\n", end="")

