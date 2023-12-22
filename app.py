from flask import Flask
app = Flask(__name__)

from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

@app.route('/')
def hello_world():
    my_string = 'Hello, World! Servera laiks' + current_time
    return my_string
