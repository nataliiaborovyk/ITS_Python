from flask import Flask, url_for, render_template, jsonify


app = Flask(__name__)


UTENTI = [
    {"username": "alice", "nome": "Alice", "cognome": "Rossi"},
    {"username": "bob",   "nome": "Bob",   "cognome": "Bianchi"},
    {"username": "nat",   "nome": "Nat",   "cognome": "K."},
]

POSTS = [
    {"id": 1, "title": "Primo post",  "body": "Contenuto del primo post...",  "author": "alice"},
    {"id": 2, "title": "Secondo post","body": "Qualche riga interessante...", "author": "bob"},
    {"id": 3, "title": "Flask è top", "body": "Adoro url_for e i template!",  "author": "nat"},
]



@app.route('/')
def home() -> str:
    return render_template('home.html')

@app.route('/about')
def about() -> str:
    return render_template('about.html')


@app.route('/user/<string:name>')
def benvenuto(name: str) -> str:
    return jsonify({"name" : name})

@app.route('/square/<int:n>')
def square(n:int) -> str:
    risultato = n ** 2
    return render_template('square.html', n=n, risultato = risultato)

@app.route('/sum/<int:a>/<int:b>')
def sum(a:int, b:int) -> str:
    risultato = a + b
    return render_template('sum.html', a=a, b=b, risultato=risultato)

@app.route('/utenti', methods=['GET'])
def utenti() -> str:
    return render_template('utenti.html', utenti=UTENTI)

@app.route('/profilo/<string:username>')
def profilo(username:str) -> str:
    # cerciamo utente nella lista
    utente_trovato = None
    for i in UTENTI:
        if i["username"] == username:
            utente_trovato = i
            break
    # cerchiamo i post scritti da quel utente
    posts_autore = []
    for i in POSTS:
        if i["author"] == username:
            posts_autore.append(i)
    # inviamo tutto al template
    return render_template('profilo.html', utente=utente_trovato, posts=posts_autore)

@app.route('/posts')
def posts() -> str:
    return render_template('posts.html', posts=POSTS)

@app.route('/post/<int:id>')
def post(id:int) -> str:
    # cerco il post con quel id
    post_trovato = None
    for i in POSTS:
        if i["id"] == id:
            post_trovato = i
            break
    #cerco attore del post
    autore = None
    if post_trovato:
        for i in UTENTI:
            if i["username"] == post_trovato["author"]:
                autore = i
                break
    # invio i dati a template
    return render_template('post.html', post=post_trovato, autore=autore)


