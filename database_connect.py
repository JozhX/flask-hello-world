import psycopg2 

# Connect to the database 
def db_connect():
    conn = psycopg2.connect(
    database="omniva", 
    user="admin", 
    password="f0HAF7ajv4JUTLHHsTrh8OTA1hGKGVOs", 
    host="dpg-cm359ben7f5s73blkisg-a", 
    port="5432") 
    return conn
  
# create a cursor
def cursor():
    cur = db_connect.cursor()
    return cur