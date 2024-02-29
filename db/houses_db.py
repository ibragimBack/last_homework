import sqlite3
from pathlib import Path

class Houses_db:
    def __init__(self):
        self.connection = sqlite3.connect(Path(__file__).parent.parent / 'house.sqlite3')
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute('DROP TABLE IF EXISTS houses')
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS houses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        price INTEGER,
        address INTEGER
        )
        ''')
        self.connection.commit()

    def insert_houses_table(self, data: dict):
        print(data)
        self.cursor.execute('''
        INSERT INTO houses(title, price, address)
        VALUES(:title, :price, :address);
        ''',
                            {
                                'title': data['title'],
                                'price': data['price'],
                                'address': data['address']
                            })
        self.connection.commit()

if __name__ == '__main__':
    db_houses = Houses_db()
    db_houses.create_table()