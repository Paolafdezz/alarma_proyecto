import mysql.connector
from mysql.connector import errorcode
import time

class DDBB:

    config = {
        'user': 'root',
        'password': 'OjoCuidao',
        'host': 'localhost',
        'port': 3306,
        'database': 'alarma',
        'raise_on_warnings': True
    }

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
            cnx.close()

    def query_alarmas(self, cursor):
        # Consulta para obtener todas las aulas y sus profesores
        cursor.execute("""
        SELECT id, hora FROM alarma;
        """)
        for (id, hora) in cursor:
            print(id, hora)
            time.sleep(0.2)

    def listar_alarmas(self):
        self.execute_query(self.query_alarmas)


# INSERT INTO `alarma`.`alarma` (`hora`) VALUES ('14:00');

if __name__ == "__main__":
    database = DDBB()
    database.listar_alarmas()