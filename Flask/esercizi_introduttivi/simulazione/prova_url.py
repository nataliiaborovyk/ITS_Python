from flask import url_for
from app import app

with app.test_request_context():
    print(url_for('home'))
    print(url_for('about'))
    print(url_for('benvenuto', name='Alice'))
    print(url_for('square', n=4))
    print(url_for('sum', a=36, b=76))


# versione con url assoluto

with app.test_request_context(base_url='http://localhost:4000'):
    print(url_for('home', _external=True))
    print(url_for('about', _external=True))
    print(url_for('benvenuto', name='Alice', _external=True))
    print(url_for('square', n=4, _external=True))
    print(url_for('sum', a=36, b=76, _external=True))
