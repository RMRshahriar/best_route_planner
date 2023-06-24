import mysql.connector



# Database connection details
config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'cse_404'
}

# Create a connection
cnx = mysql.connector.connect(**config)

# Create a cursor
cursor = cnx.cursor()
# Query to retrieve data from the table
query = "SELECT * FROM i_values"
cursor.execute(query)

# Fetch all rows from the result
rows = cursor.fetchall()

i_values = [x for x in rows[len(rows)-1] ]

print(i_values)

# Close the cursor and the connection
cursor.close()
cnx.close()
