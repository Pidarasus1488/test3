from flask import Flask
import random

app = Flask(__name__)
facts_list = ['venom', 'happy', 'teamwork', 'merry chrismas']
@app.route("/")
def hello_world():
    return f'<p>{random.choice(facts_list)}</p>

@app.route("/secret")
def secret():
    return '<h1>Secret</h1>'
app.run(debug=True)