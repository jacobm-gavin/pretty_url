import sqlite3
import os

class db ():
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

    

    def enterLinkIntoDatabase(self, full_link, shortened_link):
        
        c = self.conn.cursor()
        c.execute('INSERT INTO links (shortenedlink, fulllink) VALUES (?, ?)', (shortened_link, full_link))
        self.conn.commit()
        return True
    
    def getFullLinkFromShortLink(self, shortened_link):
        conn = sqlite3.connect('db/userlinks.db')
        c = conn.cursor()
        c.execute('SELECT fulllink FROM links WHERE shortenedlink = ?', (shortened_link,))
        full_link = c.fetchone()
        return full_link[0]
    
    def sandbox(self):
        while True:
            try:
                print(self.query(input('Enter SQL Query: ')))
            except(sqlite3.Error) as e:
                print(e)
                print('Error with SQL Query')
                continue

x = db('userlinks.db')
x.sandbox()


#x.query('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT)')
#x.query('INSERT INTO users (name, email, password) VALUES ("John Doe", "jj", "123")')
#print(x.query('SELECT * FROM users'))