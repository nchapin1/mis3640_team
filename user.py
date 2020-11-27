# https://docs.python.org/3/library/sqlite3.html
import sqlite3
conn = sqlite3.connect('user_information.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE users
(firstname text, lastname text, email text)''')

# Insert row of data
c.execute("INSERT INTO users VALUES ()")

# Save (commit) changes
conn.commit()

# Close the connection 
conn.close()