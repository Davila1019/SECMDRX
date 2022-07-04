import sqlite3

class Conexion:
    def __init__(self):
        self._conexion = sqlite3.connect("SECMDRX.db")
        try:
            self._conexion.execute("""CREATE TABLE simulacion (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nombre VARCHAR(30))""" )
            print('se creo la base de datos SECMDRX.db')
        except:
            print('La tabla ya existe')

if __name__ == "__main__":
    c = Conexion()