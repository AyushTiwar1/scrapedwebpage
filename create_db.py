"""import sqlite3
conn = sqlite3.connect('scraped_data.db')
c = conn.cursor()
c.execute('''CREATE TABLE reviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                text TEXT,
                style_name TEXT,
                color TEXT,
                verified_purchase TEXT
            )''')
conn.commit()
conn.close()"""
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import nltk
nltk.download('vader_lexicon')


