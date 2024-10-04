import sqlite3

def create_db():
    print("Criando o banco de dados e as tabelas...")
    conn = sqlite3.connect('database.db')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS customer (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            cpf TEXT NOT NULL,
            email TEXT NOT NULL,
            mobile_phone TEXT NOT NULL,
            landline_phone TEXT,
            gender TEXT,
            birthdate TEXT,
            postal_code TEXT,
            address TEXT,
            number TEXT,
            complement TEXT,
            reference TEXT,
            neighborhood TEXT,
            city TEXT,
            state TEXT
        )
    ''')

    conn.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            transaction_id TEXT NOT NULL,
            transaction_total REAL NOT NULL,
            order_date TEXT NOT NULL,
            customer_email TEXT NOT NULL,
            FOREIGN KEY (customer_email) REFERENCES customer(email)
        )
    ''')

    conn.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id TEXT NOT NULL,
            product_name TEXT NOT NULL,
            price REAL NOT NULL,
            brand TEXT,
            category TEXT,
            subcategory TEXT
        )
    ''')

    conn.execute('''
        CREATE TABLE IF NOT EXISTS newsletter (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT,
            source_id TEXT NOT NULL
        )
    ''')
    
    conn.close()
