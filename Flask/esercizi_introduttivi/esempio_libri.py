from __future__ import annotations

from flask import Flask, url_for, jsonify, request

app = Flask(__name__)

elenco_libri: dict[str, int] = {
    "Python": 5,
    "BD": 4,
    "IA": 3,
    "Progettazione": 6,
}

def libro_esiste(nome: str) -> bool:
    return nome in elenco_libri


def costruisci_dict_libro(nome: str) -> dict[str, object]:
    quantita = elenco_libri[nome]
    link = url_for("get_libro", nome=nome)
    return {
        "nome": nome,
        "quantita": quantita,
        "link": link,
    }


@app.route("/libro/<string:nome>", methods=["GET"])
def get_libro(nome: str):
    if not libro_esiste(nome):
        return (
            jsonify({"errore": f"Non esiste un libro con nome '{nome}'."}),
            404,
        )
    libro_dict = costruisci_dict_libro(nome)
    return jsonify(libro_dict), 200


@app.route("/libri", methods=["GET"])
def get_libri():
    risultato: list[dict[str, object]] = []
    for nome in elenco_libri:
        libro_dict = costruisci_dict_libro(nome)
        risultato.append(libro_dict)
    return jsonify(risultato), 200


@app.route("/libri", methods=["POST"])
def crea_libro():
    """
    Si aspetta un JSON del tipo:
        {
            "nome": "NuovoLibro",
            "quantita": 7
        }
    """
    dati = request.get_json()

    if dati is None:
        return jsonify({"errore": "Body della richiesta mancante o non in formato JSON."}), 400

    nome = dati.get("nome")
    quantita = dati.get("quantita")

    if nome is None or quantita is None:
        return jsonify({"errore": "I campi 'nome' e 'quantita' sono obbligatori."}), 400
    if not isinstance(nome, str) or nome.strip() == "":
        return jsonify({"errore": "Il campo 'nome' deve essere una stringa non vuota."}), 400
    if not isinstance(quantita, int) or quantita < 0:
        return jsonify({"errore": "Il campo 'quantita' deve essere un intero >= 0."}), 400
    if libro_esiste(nome):
        return jsonify({"errore": f"Esiste già un libro con nome '{nome}'."}), 400

    elenco_libri[nome] = quantita

    libro_creato = costruisci_dict_libro(nome)
    return jsonify({"stato": "creato", "libro": libro_creato}), 201
