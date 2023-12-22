from flask import Flask
app = Flask(__name__)

from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

@app.route('/')
def hello_world():
    my_string = '<h1 style="text-align:center">Hello, World!</h1>' + '<h2 style="text-align:center">Servera laiks ' + current_time + '</h2>'
    return my_string
