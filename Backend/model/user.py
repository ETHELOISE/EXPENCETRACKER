import sqlite3


class User:
    table_name = "users"
    def __init__(self ,id=None ,name=None ,email=None ,password=None) -> None : 
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def save(self):
        if  self.id:
            with sqlite3.connect("db.db") as conn:
                cursor = conn.cursor()
                query = f'update {self.table_name} set name=? ,email=? ,password=? where id=? '
                cursor.execute(query ,(self.name ,self.email ,self.password ,self.id))

        else :
            with sqlite3.connect("db.db") as conn:
                cursor = conn.cursor()
                query = f"insert into {self.table_name}(name, email ,password) values (?,?,?) "
                cursor.execute(query ,(self.name ,self.email ,self.password))

    def read(id=None):
        if id :
            with sqlite3.connect("db.db") as conn:
                cursor = conn.cursor()
                query = f"select * from {__class__.table_name} where id =?"
                result = cursor.execute(query ,(id,)).fetchone()
                return result
        else :
            with sqlite3.connect('db.db') as conn:
                cursor = conn.cursor()
                query = f"select * from {__class__.table_name} "
                result = cursor.execute(query ,()).fetchall()
                return result

    def delete(id):
        with sqlite3.connect("db.db") as conn:
            cursor = conn.cursor()
            query = f"delete from {__class__.table_name} where id= ?"
            cursor.execute(query ,(id ,))


