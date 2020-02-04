import sqlite3

class BooksDatabase:

    def __init__(self):#Same as constructor
        self.conn=sqlite3.connect("books.db")
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year INTEGER, isbn INTEGER)")
        self.conn.commit()

    def insert(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO book values (NULL,?,?,?,?)",(title,author,year,isbn)) #Python understands that NULL will be ID
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * from book")
        rows=self.cur.fetchall()
        #self.conn.commit() Since this is just a select operation, we don't need to commit
        return rows

    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * from book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        rows=self.cur.fetchall()
        #self.conn.commit() Since this is just a select operation, we don't need to commit
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,)) #Python understands that NULL will be ID
        self.conn.commit()

    def update(self,id,title,author,year,isbn):

        self.cur.execute("UPDATE book SET title=?, author=?, year=?,isbn=? WHERE id=?",(title,author,year,isbn,id)) #Python understands that NULL will be ID
        self.conn.commit()

    def __del__(self):#called when object is destroyed
        self.conn.close()

#connect() #connect function will run as soon as backend is imported in frontend.

#insert("The Moon","Dewang Shah",1999,92374543835)
#update(3,"The Sun","Dewang Shah",1999,92374543835)
#print(view())
#delete(2)
#print(search(author="John Smith"))
#print(view())
