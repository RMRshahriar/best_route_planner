import mysql.connector
import time
import backend

config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'cse_404'
}
cnx = mysql.connector.connect(**config)

cursor = cnx.cursor()

query = "SELECT * FROM i_values"
cursor.execute(query)

rows = cursor.fetchall()

pn = n = len(rows)
while True :
    cnx = mysql.connector.connect(**config)

    cursor = cnx.cursor()
    
    query = "SELECT * FROM i_values"
    cursor.execute(query)

    rows = cursor.fetchall()
    n = len(rows)
    if n > pn :
        print('new input')
        pn = n
        print(pn,n)
        backend.backend()
    time.sleep(1)
        
    

