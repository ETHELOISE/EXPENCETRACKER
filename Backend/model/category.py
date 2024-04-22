
import sqlite3

class Category:
    table_name = "category"
    def __init__(self ,id=None ,name=None ) -> None : 
        self.id = id
        self.name = name


    def save(self ,id=None):
        if  id:
            with sqlite3.connect("db.db") as conn:
                cursor = conn.cursor()
                query = f'update {self.table_name} set name=?  where id=? '
                cursor.execute(query ,(self.name ,self.id))

        else :
            with sqlite3.connect("db.db") as conn:
                cursor = conn.cursor()
                query = f"insert into {self.table_name}(name) values (?,?,?) "
                cursor.execute(query ,(self.name ))

    def read(id=None):
        if id :
            with sqlite3.connect("db.db") as conn:
                cursor = conn.cursor()
                query = f"select * from {__class__.table_name} where id =?"
                result = cursor.execute(query ,(id,))
                return result
        else :
            with sqlite3.connect('db.db') as conn:
                cursor = conn.cursor()
                query = f"select * from {__class__.table_name} "
                result = cursor.execute(query ,())
                return result

    def delete(id):
        with sqlite3.connect("db.db") as conn:
            cursor = conn.cursor()
            query = f"delete from {__class__.table_name} where id= ?"
            cursor.execute(query ,(id ,))
