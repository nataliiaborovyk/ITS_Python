'''
Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di creare, modificare, e cercare ricette basate sugli ingredienti. Il sistema dovrà essere capace di gestire una collezione (dizionario) di ricette e i loro ingredienti.

Classe:
- RecipeManager:
    Gestisce tutte le operazioni legate alle ricette.

    Metodi:
    - create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una lista di ingredienti. Restituisce un nuovo dizionario con la sola ricetta appena creata o un messaggio di errore se la ricetta esiste già.

    - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.

    - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

    - update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente con un altro nella ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

    - list_recipes(): Elenca tutte le ricette esistenti.

    - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta. Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.

    - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente. Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.
'''

class RecipeManager:

    def __init__(self) -> None:
        self.collezione = {}

    def create_recipe(self, name:str, ingredients:list[str]) -> dict | None:
        if name in self.collezione:
            print("La ricetta esiste gia")
        else:
            self.collezione[name] = ingredients
            return {name: self.collezione[name]}

    def add_ingredients(self, recipe_name:str, ingredient:str) -> None:
        if recipe_name not in self.collezione or ingredient in self.collezione[recipe_name]:
            print("Ingrediente esiste gia o ricetta non esiste")
        else:
            self.collezione[recipe_name].append(ingredient)
            return {recipe_name: self.collezione[recipe_name]}

    def remove_ingredient(self, recipe_name:str, ingredient: str) -> None:
        if recipe_name not in self.collezione or ingredient not in self.collezione[recipe_name]:
            print("ingrediente non è presente o la ricetta non esiste")
        else:
            self.collezione[recipe_name].remove(ingredient)
            return {recipe_name: self.collezione[recipe_name]}

    def update_ingredient(self, recipe_name:str, old_ingredient:str, new_ingredient:str) -> None:
        if recipe_name not in self.collezione or old_ingredient not in self.collezione[recipe_name]:
            print ("ingrediente non è presente o la ricetta non esiste")
        else:
            for v in self.collezione.values():
                if old_ingredient in v:
                    index_ing: int = v.index(old_ingredient)
                    v.pop(index_ing)
                    v.insert(index_ing, new_ingredient)
            return {recipe_name: self.collezione[recipe_name]}
        
    def list_recipes(self) -> dict[str, list[str]]:
        ricette: list = [k for k in self.collezione.keys()]
        return ricette
    
    def list_ingredients(self, recipe_name:str) -> list[str]:
        if recipe_name not in self.collezione:
            print("la ricetta non esiste")
        else:
            return self.collezione[recipe_name]
        
    def search_recipe_by_ingredient(self, ingredient:str) -> dict:
        elenco: dict = {}
        for k,v in self.collezione.items():
            if ingredient in v:
                elenco[k] = v
        if not elenco:
            print("nessuna ricetta contiene l'ingrediente")
        else:
            return elenco