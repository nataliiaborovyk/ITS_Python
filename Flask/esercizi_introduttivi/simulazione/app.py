from flask import Flask, url_for, jsonify

app = Flask(__name__)



lista_utenti: dict[str,int] = {
    "Alice": 25,
    "Bob": 18,
    "Elis": 37,
    "Biagio": 41
     }

lista_posts: list[dict] = [
    {"id": 1, "title": "Primo post",   "text": "Contenuto del primo post...",  "author": "Alice"},
    {"id": 2, "title": "Appunti Flask","text": "Oggi ho imparato url_for.",    "author": "Bob"},
    {"id": 3, "title": "Pensieri",     "text": "Mini blog senza template.",    "author": "Elis"},
]

# browser legge tag html nella stringa e lo renderizza

@app.route('/')
def home() -> str:
    links = [
        f'<li><a href="{url_for("about")}">/about</a></li>',
        f'<li><a href="{url_for("benvenuto", name="Nat")}">/user/Nat</a></li>',
        f'<li><a href="{url_for("square", n=5)}">/square/5</a></li>',
        f'<li><a href="{url_for("sum", a=3, b=7)}">/sum/3/7</a></li>',
        f'<li><a href="{url_for("user", name="Mark", age=37)}">/user</a></li>',
        f'<li><a href="{url_for("utenti")}">/utenti</a></li>',
        f'<li><a href="{url_for("utenti2")}">/utenti (tramite user)</a></li>',
        f'<li><a href="{url_for("post", id=1)}">/post</a></li>',
        f'<li><a href="{url_for("posts")}">/posts</a></li>',
        f'<li><a href="{url_for("posts2")}">/posts (tramite post)</a></li>'
    ]
    return "<h3>Tutti esercizi insieme</h3>  <ul>" + "".join(links) + "</ul>"

@app.route('/about')
def about() -> str:
    return "<h3>Nuovo esercizio, studio come si usa  flask </h3>"


@app.route('/user/<string:name>')
def benvenuto(name: str) -> str:
    return f"<h1>Benvenuto, {name}!</h1>"
        
@app.route('/square/<int:n>')
def square(n:int) -> str:
    risultato = n ** 2
    return f"<p>Numero {n} ** 2 = {risultato}</p>"
        
@app.route('/sum/<int:a>/<int:b>', methods=['GET'])
def sum(a:int, b:int) -> str:
    risultato = a + b
    #return f"<p>Somma di {a} + {b} = {risultato}</p>"
    return jsonify(risultato)


@app.route('/user/<string:name>/age/<int:age>', methods=['GET'])
def user(name: str, age: int) -> str:
    url = url_for('user', name=name, age=age)  # → /user/<name>
    #return  f"<h4>Profilo di {name}, age={age}:   {url},  Link: <a href='{url}'>{url}</a></h4>"
    return jsonify({"Name": name, "age":age, "Url": url})


@app.route("/utenti")
def utenti() -> str:
    righe = []
    utenti:list = []
    for k, v in lista_utenti.items():
        url = url_for("user", name=k, age=v)
        #righe.append(f"<p>Profilo di {k}, age={v}: <a>{url}</a> <p>Link: <a href='{url}'>{url}</a></p>")
        utenti.append({"name":k, "age":v, "link":url})
    #return "\n".join(righe)
    return jsonify(utenti)
    
  
@app.route("/utenti2")
def utenti2() -> str:
    righe = ['<h1>Creo lista utenti usando route user</h1>']
    for k, v in lista_utenti.items():
        url = url_for("user", name=k, age=v)
        righe.append(user(k, v))
    return "\n".join(righe)

@app.route("/post/<int:id>")
def post(id: int) -> str:
    for i in lista_posts:
        if i['id'] == id:
            url = url_for('post', id=id)
    #         return (
    #             f"<p>ID: {i['id']}</p>"
    #             f"<p>Autore: {i['author']}</p>"
    #             f"<p>Title: {i['title']}</p>"
    #             f"<p>Testo: {i['text']}</p>"
    #             f"<p> URL: {url} </p> "
    #             f"<p> Link: <a href='{url}'> {url}</a> </p> "
    #         )
            return jsonify({"ID":i['id'], "autore":i['author'], "Title":i['title'], "Testo": i['text'], "link": url })
    return jsonify(f"Non esiste post con numero {id}")
    # return f"Non esiste il post con id {id} "



@app.route("/posts")
def posts() -> str:
    righe = []
    for i in lista_posts:
        for k, v in i.items():
            righe.append(f"<p>{k}: {v}</p>")
        url = url_for("post", id=i['id'])
        righe.append(url)
        righe.append("<hr>")
    return "\n".join(righe), 200

@app.route("/posts2")
def posts2() -> str:
    righe = []
    for i in lista_posts:
        righe.append(post(i['id']))
        righe.append("<hr>")
    return "\n".join(righe)






