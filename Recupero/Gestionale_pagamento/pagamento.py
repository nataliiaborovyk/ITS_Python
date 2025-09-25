

class Pagamento:

    __importo: float

    def __init__(self) -> None:
        self.__importo = 0.0

    def set_importo(self, importo: float) -> None:
        self.__importo = importo

    def get_importo(self) -> float:
        return self.__importo
    
    def dettagliPagamento(self) -> str:
        importo_r: float = round(self.get_importo(), 2)
        return f"Importo del pagamento: {importo_r}"


class PagamentoContanti(Pagamento):

    def __init__(self) -> None:
        super().__init__()

    def dettagliPagamento(self):
        importo_cont: str = super().dettagliPagamento()
        return f"{importo_cont} in contanti"
    
    def inPezziDa(self) -> str:
        banconote: list = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.01]
        importo: float = self.get_importo()
        import_r: float = round(importo, 2)

        for i in banconote:
            quantita:int = import_r // i
            if quantita > 0:
                if i >= 5:
                    if quantita > 1:
                        print(f"{quantita} banconote da {i}$")
                    else:
                        print(f"{quantita} banconota da {i}$")
                else:
                    if quantita > 1:
                        print(f"{quantita} monete da {i}$")
                    else:
                        print(f"{quantita} moneta da {i}$")
                import_r = import_r % i

    
class PagamentoCartaDiCredito(Pagamento):

    __nome_titolare: str
    __scadenza: str
    __numero_carta: int

    def __init__(self, nome: str, scadenza: str, numero_carta: int) -> None:
        self.__nome_titolare = nome
        self.__scadenza = scadenza
        self.__numero_carta = numero_carta

    def dettagliPagamento(self):
        importo: float = super().dettagliPagamento()
        return f"{importo} effettuato con la carta di credito\nNome sulla carta: {self.__nome_titolare}\nData di scadenza: {self.__scadenza}\nNumero della carta: {self.__numero_carta}"


if __name__ == "__main__":

    p1:Pagamento = Pagamento()
    print(p1.get_importo())

    p1.set_importo(485)
    print(p1.get_importo())

    print(p1.dettagliPagamento())

    p2:PagamentoContanti = PagamentoContanti()
    print(p2.dettagliPagamento())
    p2.set_importo(205)
    print(p2.dettagliPagamento())
    p2.inPezziDa()

    p3:PagamentoCartaDiCredito = PagamentoCartaDiCredito("Nat", "15/30", 6528846256746252)
    p3.set_importo(797)
    print(p3.dettagliPagamento())

    p2:PagamentoContanti = PagamentoContanti()
    p2.set_importo(13.74)
    p2.inPezziDa()
    print(p2.dettagliPagamento())

    