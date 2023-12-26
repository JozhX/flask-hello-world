from flask import Flask, render_template, request, redirect, url_for 
from database_connect import db_connect, cursor
app = Flask(__name__)

###########################################################

@app.route('/')
def main_page():
    cursor.execute('SELECT zip,nosaukums FROM omniva;') 
    pakomati = cursor.fetchall()
    cursor.close()
    db_connect.close()
    return render_template('index.html', data=pakomati)

@app.route('/update', methods=['POST']) 
def update(): 
    # Get the data from the form 
    zip = request.form['zip'] 
    nosaukums = request.form['nosaukums'] 
  
    # Update the data in the table 
    cursor.execute('UPDATE products SET nosaukums=%s WHERE zip=%s', (nosaukums, zip)) 
  
    # commit the changes 
    db_connect.commit() 
    cursor.close()
    db_connect.close()
    return redirect(url_for('index')) 

import database_reset