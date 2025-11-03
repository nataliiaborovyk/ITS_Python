from flask import Flask, url_for
app = Flask(__name__)

#app.run(debug=True, host='127.0.0.1', port=4000)

@app.route('/')
def nome() -> str:
    return"<h3>Hello,word!</h3>"


@app.route('/dataanalyst')
def show_user() -> str:
    return "Sei uno studente di dataAnalist"


@app.route('/user/<string:username>/<int:age>')
def show_user_profile(username: str, age:int) -> str:
    return f"Profilo di {username} e eta {age}"

@app.route('/post/<int:post_id>')
def show_post(post_id: int) -> str:
    return f"Post {post_id}"

with app.test_request_context():
    print(url_for('nome'))
    print(url_for('show_user_profile', username='John Doe', age=28))
    print(url_for('show_post', post_id=42))

    