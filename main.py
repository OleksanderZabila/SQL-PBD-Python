import sqlite3

connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
cursor.execute("INSERT INTO users (username, password) VALUES ('user', 'user123')")
connection.commit()

def demonstrate_sql_injection(cursor, user_input):
    query = f"SELECT * FROM users WHERE username = 'admin' AND password = '{user_input}'"
    print("Небезпечний запит:")
    for row in cursor.execute(query):
        print(row)

def demonstrate_safe_query(cursor, username, password):
    safe_query = "SELECT * FROM users WHERE username = ? AND password = ?"
    print("\nЗахищений запит:")
    for row in cursor.execute(safe_query, (username, password)):
        print(row)

user_input = "' OR '1'='1"

demonstrate_sql_injection(cursor, user_input)

username = 'admin'
password = user_input
demonstrate_safe_query(cursor, username, password)

connection.close()
