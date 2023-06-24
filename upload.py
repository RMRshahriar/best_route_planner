import mysql.connector



mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='cse_404'
)

mycursor = mydb.cursor()

route = 'a'
cost = 0

sql = ("INSERT INTO best_route(route, cost)"
    "VALUES (%s, %s)")

val = [
    (route , cost)
]

mycursor.executemany(sql, val)
mydb.commit()
        
