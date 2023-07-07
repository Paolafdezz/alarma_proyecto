import mysql.connector
from mysql.connector import errorcode
import time


class DDBB:
    config = {
        "user": "root",
        "password": "OjoCuidao",
        "host": "localhost",
        "port": 3306,
        "database": "alarma",
        "raise_on_warnings": True,
    }

    def __init__(self, *args, **kwargs):
        self.results = None
        self.hora = "00:00"

    def execute_query(self, callback):
        try:
            cnx = mysql.connector.connect(**self.config)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Algo está mal con el nombre de usuario o contraseña")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("La base de datos no existe")
            else:
                print(err)

        else:
            with cnx.cursor() as cursor:
                callback(cursor)
            cnx.commit()
            cnx.close()

    def query_alarmas(self, cursor):
        cursor.execute(
            """
        SELECT id, hora FROM alarma;
        """
        )

        for id, hora in cursor:
            print(id, hora)

    def listar_alarmas(self):
        self.execute_query(self.query_alarmas)

    def query_insertar_alarma(self, cursor):
        query = f"INSERT INTO `alarma`.`alarma` (`hora`) VALUES ('{self.hora}');"
        datos = cursor.execute(query)

    def insertar_alarma(self, hora):
        self.hora = hora
        self.execute_query(self.query_insertar_alarma)


if __name__ == "__main__":
    from random import randint

    database = DDBB()
    database.insertar_alarma(f"{randint(0,24)}:{randint(0,60)}")
    database.listar_alarmas()
