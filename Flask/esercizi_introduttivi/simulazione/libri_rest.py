from __future__ import annotations

from flask import Flask, url_for, jsonify, request

app = Flask(__name__)

# Dizionario che simula un piccolo "database" di libri.
# chiave: nome del libro (str)
# valore: quantità disponibile (int)
elenco_libri: dict[str, int] = {
    "Python": 5,
    "BD": 4,
    "IA": 3,
    "Progettazione": 6,
}


# --------------------- FUNZIONI DI SUPPORTO (STILE PROF) ---------------------


def libro_esiste(nome: str) -> bool:
    """Ritorna True se il libro è presente nell'elenco."""
    return nome in elenco_libri


def costruisci_dict_libro(nome: str) -> dict[str, object]:
    """Costruisce un dizionario con le informazioni di un libro, in stile API."""
    quantita = elenco_libri[nome]
    link = url_for("get_libro", nome=nome)
    return {
        "nome": nome,
        "quantita": quantita,
        "link": link,
    }


# ---------------------------- ENDPOINT: GET /libro/<nome> ----------------------------


@app.route("/libro/<string:nome>", methods=["GET"])
def get_libro(nome: str):
    """
    Restituisce le informazioni di un singolo libro.
    Se il libro non esiste, ritorna errore 404.
    """
    if not libro_esiste(nome):
        return (
            jsonify({"errore": f"Non esiste un libro con nome '{nome}'."}),
            404,
        )

    libro_dict = costruisci_dict_libro(nome)
    return jsonify(libro_dict), 200


# ---------------------------- ENDPOINT: GET /libri ----------------------------


@app.route("/libri", methods=["GET"])
def get_libri():
    """
    Restituisce la lista di tutti i libri.
    Ogni libro è rappresentato come dizionario con:
    - nome
    - quantita
    - link alla risorsa singola (/libro/<nome>)
    """
    risultato: list[dict[str, object]] = []

    for nome in elenco_libri:
        libro_dict = costruisci_dict_libro(nome)
        risultato.append(libro_dict)

    return jsonify(risultato), 200


# ---------------------------- ENDPOINT: POST /libri ----------------------------


@app.route("/libri", methods=["POST"])
def crea_libro():
    """
    Crea un nuovo libro.
    Si aspetta un JSON del tipo:
        {
            "nome": "NuovoLibro",
            "quantita": 7
        }

    Casi gestiti:
    - dati mancanti -> 400
    - libro già esistente -> 400
    - quantita non valida -> 400
    - creazione corretta -> 201
    """
    dati = request.get_json()

    if dati is None:
        return jsonify({"errore": "Body della richiesta mancante o non in formato JSON."}), 400

    nome = dati.get("nome")
    quantita = dati.get("quantita")

    # Controllo campi obbligatori
    if nome is None or quantita is None:
        return jsonify({"errore": "I campi 'nome' e 'quantita' sono obbligatori."}), 400

    # Controllo che il nome sia una stringa non vuota
    if not isinstance(nome, str) or nome.strip() == "":
        return jsonify({"errore": "Il campo 'nome' deve essere una stringa non vuota."}), 400

    # Controllo che la quantità sia un intero >= 0
    if not isinstance(quantita, int) or quantita < 0:
        return jsonify({"errore": "Il campo 'quantita' deve essere un intero >= 0."}), 400

    # Controllo libro già esistente
    if libro_esiste(nome):
        return jsonify({"errore": f"Esiste già un libro con nome '{nome}'."}), 400

    # Inserisco il libro nel "database" in memoria
    elenco_libri[nome] = quantita

    # Costruisco il risultato in stile prof
    libro_creato = costruisci_dict_libro(nome)
    return jsonify({"stato": "creato", "libro": libro_creato}), 201
