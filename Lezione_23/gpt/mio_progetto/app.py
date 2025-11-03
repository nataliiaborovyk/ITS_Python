from flask import Flask, render_template, url_for

app = Flask(__name__)

# @app.route('/')
# def home():
#     nome = "Nat"
#     return render_template('home.html', nome=nome)


# Pagina principale
@app.route('/')
def home():
    nome = "Nat"
    # Costruiamo automaticamente il link al profilo con url_for()
    link_profilo = url_for('profilo', username=nome)  # Flask costruisce /profilo/Nat
    return render_template('home.html', nome=nome, link_profilo=link_profilo)

# Pagina del profilo
@app.route('/profilo/<string:username>')
def profilo(username:str):
    return render_template('profilo.html', username=username)

# Avvio server locale
if __name__ == '__main__':
    app.run(port=4000, debug=True)
