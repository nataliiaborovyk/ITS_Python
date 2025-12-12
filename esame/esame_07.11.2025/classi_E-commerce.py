'''

Sistema E-commerce
Progetta e implementa un semplice sistema e-commerce in Python, organizzato attorno a tre classi principali: Product, ShoppingCart e Shop.
 Ogni classe deve essere chiara nel proprio scopo e ogni funzione deve essere documentata con responsabilità ben definite.

Classe Product
Rappresenta un singolo prodotto venduto nel negozio online.
 Ogni prodotto ha informazioni uniche e uno stock che ne regola la disponibilità.

Attributi
    product_id: str — Identificatore unico del prodotto nello shop (esempio: "SKU1234").
    Serve per distinguere ogni articolo.
    name: str — Nome del prodotto (esempio: "Mouse Wireless Logitech").
    price: float — Prezzo unitario del prodotto in euro (ad esempio 29.90).
    stock: int — Quantità attualmente disponibile a magazzino per il prodotto.

Metodi
    update_stock(quantity: int) -> None
    Aggiorna la quantità disponibile del prodotto.
    Se il parametro è positivo la quantità viene aumentata, se negativo viene diminuita.
    Non restituisce nulla.

    is_available(quantity: int) -> bool
    Controlla se il prodotto ha almeno la quantità richiesta disponibile (utile per le vendite).
    Ritorna True se lo stock è sufficiente, False altrimenti.


Classe ShoppingCart
Questa classe simula il carrello di un utente, che può contenere più prodotti con relative quantità.
 Opera come contenitore temporaneo fino al momento del pagamento.

Attributi
    items: dict[str, int] — Dizionario che associa ogni product_id alla quantità richiesta da acquistare da parte dell’utente.
    Esempio: { 'SKU1234': 2, 'SKU5678': 1 }.

Metodi
    add_item(product: Product, quantity: int) -> str
    Tenta di aggiungere il prodotto al carrello nella quantità richiesta.
    Se la quantità disponibile non è sufficiente, restituisce un messaggio di errore.
    Se l’aggiunta va a buon fine, aggiorna lo stock del prodotto (diminuisce di quantity) e ritorna un messaggio di conferma.

    remove_item(product_id: str) -> str
    Rimuove dal carrello il prodotto corrispondente al product_id.
    Se il prodotto era presente, lo elimina e restituisce conferma; se non era presente, restituisce un messaggio di errore.

    get_total(products: dict[str, Product]) -> float
    Calcola e ritorna la somma totale degli articoli nel carrello, moltiplicando il prezzo unitario per la quantità di ogni prodotto.
    Ha bisogno del dizionario dei prodotti per accedere ai prezzi.

    clear() -> None
    Svuota tutto il carrello, rimuovendo tutti i prodotti e le relative quantità.


Classe Shop
Gestisce l’inventario dei prodotti e tutti i carrelli attivi (potrebbero corrispondere a diversi utenti o sessioni).
 Offre metodi per la gestione dei prodotti, la creazione di carrelli e la conclusione dell’acquisto (checkout).

 Attributi
    products: dict[str, Product]
    Mappa ogni product_id a un oggetto Product, rappresentando l’intero inventario del negozio.

    carts: dict[str, ShoppingCart]
    Mappa ogni carrello (identificato da un cart_id, es. "cart123") all’oggetto ShoppingCart corrispondente.
    Così si gestiscono più clienti contemporaneamente.


Metodi
    add_product(product: Product) -> str
    Aggiunge un nuovo prodotto al negozio.
    Se il product_id è già presente, non aggiunge il prodotto e restituisce un messaggio di errore;
    altrimenti, aggiunge il nuovo prodotto e ritorna una stringa di conferma.

    remove_product(product_id: str) -> str
    Rimuove il prodotto col dato product_id dall’inventario.
    Restituisce conferma se l’operazione ha successo o un errore se il prodotto non esiste.

    create_cart() -> str
    Crea un nuovo carrello della spesa, genera un nuovo cart_id (può usare ad esempio uuid),
    lo inserisce nella mappa carts e ritorna il suo id.

    checkout(cart_id: str) -> float | str
    Conclude l’acquisto per il carrello identificato da cart_id.
    Se tutti i prodotti nel carrello sono effettivamente disponibili negli stock,
    calcola il totale, aggiorna definitivamente le giacenze e svuota il carrello.
    Se manca disponibilità per uno o più prodotti durante questa verifica,
    restituisce un messaggio di errore (ad esempio specificando quali oggetti non sono disponibili)
    e non conclude l’acquisto.

Nota Bene
Ogni metodo dovrebbe controllare con precisione la validità dell’operazione richiesta e fornire messaggi chiari in caso di errore.
Si assuma che ogni cart_id e product_id sia univoco sul sistema.
L’esercizio valuterà la correttezza dell’organizzazione delle classi e delle responsabilità di ogni metodo.
'''

import uuid

class Product:
    def __init__(self, 
                 product_id: str, 
                 name: str, 
                 price: float, 
                 stock: int = 0) -> None:
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity: int) -> None:
        new: int = self.stock + quantity
        if new < 0:
            raise ValueError("stock negativo")
        self.stock = new

    def is_available(self, quantity: int) -> bool:
        if quantity < 0:
            return False
        return self.stock >= quantity

    def _get_id(self) -> str:
        return self.product_id

    def _get_price(self) -> float:
        return self.price


class ShoppingCart:
    def __init__(self) -> None:
        self.items: dict[str, int] = {}
        self.cart_id: str = str(uuid.uuid4())

    def add_item(self, product: Product, quantity: int) -> str:
        prod_id: str = product._get_id()
        if not product.is_available(quantity):
            return f"Quantità {quantity} non è disponibile"
        if prod_id not in self.items:
            self.items[prod_id] = quantity
        else:
            self.items[prod_id] += quantity
        return f"Prodotto {prod_id} in quantità {quantity} è stato aggiunto al carrello"

    def remove_item(self, product_id: str) -> str:
        if product_id not in self.items:
            return f"Prodotto {product_id} non è presente nel carrello"
        self.items.pop(product_id)
        return f"Prodotto {product_id} è stato eliminato con successo"

    def get_total(self, products: dict[str, Product]) -> float:
        sum_tot: float = 0
        for prod_id, quant in self.items.items():
            prezzo: float = products[prod_id]._get_price()
            sum_tot += prezzo * quant
        return sum_tot

    def clear(self) -> None:
        return self.items.clear()

    def _get_cart_id(self) -> str:
        return self.cart_id

    def _get_items(self) -> dict[str, int]:
        return self.items


class Shop:
    def __init__(self, 
                 products: dict[str, Product]|None = None, 
                 carts: dict[str, ShoppingCart]|None = None) -> None:
        self.products = products or {}
        self.carts = carts or {}

    def add_product(self, product: Product) -> str:
        prod_id: str = product._get_id()
        if prod_id in self.products:
            return "Errore, il prodotto è già presente"
        self.products[prod_id] = product
        return f"Prodotto {prod_id} è stato aggiunto al negozio"

    def remove_product(self, product_id: str) -> str:
        if product_id not in self.products:
            return "Prodotto non esiste nel negozio"
        self.products.pop(product_id)
        return f"Prodotto {product_id} è stato rimosso dal negozio"

    def create_cart(self) -> str:
        cart: ShoppingCart = ShoppingCart()
        cart_id: str = cart._get_cart_id()
        self.carts[cart_id] = cart
        return cart_id

    def checkout(self, cart_id: str) -> float | str:
        if cart_id not in self.carts:
            return "Carrello non esiste"

        cart: ShoppingCart = self.carts[cart_id]
        cart_prod: dict[str, int] = cart._get_items()

        non_disponibili: list[str] = []
        for prod_id in cart_prod.keys():
            if prod_id not in self.products:
                non_disponibili.append(prod_id)
                continue
            prod = self.products[prod_id]
            quant = cart_prod[prod_id]
            if not prod.is_available(quant):
                non_disponibili.append(prod_id)

        if non_disponibili:
            return f"Prodotti {non_disponibili} non sono più disponibili"

        sum_tot: float = 0
        for prod_id, quant in cart_prod.items():
            prod: Product = self.products[prod_id]
            prod.update_stock(-quant)
            prezzo: float = prod._get_price()
            sum_tot += prezzo * quant

        cart.clear()
        return sum_tot
