import psycopg2
from psycopg2.extras import RealDictCursor

DATABASE_URL = 'postgresql://postgres:postgres@localhost/otobook'

def init_db():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS books
                   (id SERIAL PRIMARY KEY, title TEXT, author TEXT, isbn TEXT, synopsis TEXT, keywords TEXT)''')
    conn.commit()
    cur.close()
    conn.close()

def save_metadata(metadata):
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute("INSERT INTO books (title, author, isbn, synopsis, keywords) VALUES (%s, %s, %s, %s, %s)",
                (metadata['title'], metadata['author'], metadata['isbn'], metadata['synopsis'], metadata['keywords']))
    conn.commit()
    cur.close()
    conn.close()

def fetch_metadata():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
