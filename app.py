from flask import Flask, render_template, request, redirect, url_for 
import psycopg2 

app = Flask(__name__)

###########################################################

# Connect to the database 
conn = psycopg2.connect(database="omniva", user="admin", 
                        password="f0HAF7ajv4JUTLHHsTrh8OTA1hGKGVOs", 
                        host="dpg-cm359ben7f5s73blkisg-a", port="5432") 
  
# create a cursor 
cur = conn.cursor() 
  
# if you already have any table or not id doesnt matter this  
# will create a products table for you. 
cur.execute("CREATE TABLE IF NOT EXISTS omniva (zip integer NOT NULL, nosaukums varchar(250) NOT NULL);") 
cur.execute("TRUNCATE TABLE omniva;") 
  
# Insert some data into the table 

  
# commit the changes 
conn.commit() 

sql = 'SELECT count(*) FROM omniva;'
cur.execute(sql) 
results = cur.fetchone() 
# results['count']
  
# close the cursor and connection 
cur.close() 
conn.close() 

###########################################################

@app.route('/')
def hello_world():
    my_string = '<h1 style="text-align:center">Ahoi, bebra kungs!!</h1>' + '<h2 style="text-align:center">Datubāzē ' + results['count'] + ' Omniva pakomāti</h2>'
    return my_string
