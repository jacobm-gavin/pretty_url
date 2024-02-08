import sqlite3
import os

class db:
    def __init__(self, name):
        if not os.path.exists('db'):
            os.makedirs('db')
        if not os.path.exists(f'db/{name}'):
            self.conn = sqlite3.connect(f'db/{name}')
            c = self.conn.cursor()
            c.execute('CREATE TABLE links (shortenedlink TEXT, fulllink TEXT)')
            self.conn.commit()
        else:
            self.conn = sqlite3.connect(f'db/{name}')
        self.cursor = self.conn.cursor()
        

    def query(self, query):
        self.cursor.execute(query)
        self.conn.commit()
        return self.cursor.fetchall()

    def sandbox(self):
        while True:
            try:
                print(self.query(input('Enter SQL Query: ')))
            except(sqlite3.Error) as e:
                print(e)
                print('Error with SQL Query')
                continue
    
    def clearTable(self):
        try:
            self.query('DELETE FROM links')
            return True
        except:
            return False
        
tester = db('userlinks.db')
tester.sandbox()
