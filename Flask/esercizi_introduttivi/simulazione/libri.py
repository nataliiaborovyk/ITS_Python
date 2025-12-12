from flask import Flask, url_for, jsonify, request

app = Flask(__name__)


elenco_libri: dict[str,int] = {
    'Python': 5,
    'BD' : 4, 
    'IA' : 3,
    'Progettazione': 6
}


@app.route("/libro/<string:nome>", methods=['GET'])
def libro(nome:str) -> str:
    if nome in elenco_libri:
        url = url_for("libro",nome=nome)
        return (f"<p>Libro: {nome}, quantita: {elenco_libri[nome]}</p>"
                f"<p>Link: <a href='{url}'>{url}</a></p>")
    else:
        return (f"<p>Non esiste</P>")
    

@app.route("/libri", methods=['GET'])
def libri() -> str:
    result = []
    for k, v in elenco_libri.items():
        url = url_for("libro", nome=k, quantita=v)
        riga = f"<p>Libro: {k}, quantita: {v}, Link: <a href='{url}'> {url} </a></p> "
        result.append(riga)
    return "\n".join(result)

@app.route("/libri", methods=['POST'])
def post_libro(nome:str, quant:int) -> str:
    dati = request.get_json()
    if nome in elenco_libri:
        return jsonify({"Errore": "Libro gia esiste"}), 400
    elenco_libri[nome] = quant
    return jsonify({"Stato": "Creato", "Libro": nome, "quantita":quant}), 201
