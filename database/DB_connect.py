import mysql.connector
from mysql.connector import errorcode
import pathlib


def get_connection() -> mysql.connector.connection:
    try:
        cnx = mysql.connector.connect(
            host="localhost",  # XAMPP default
            port=3306,
            user="root",  # XAMPP default
            password="",  # XAMPP default
            database="autonoleggio",
            use_pure=True
        )
        return cnx
    except mysql.connector.Error as err:
        print("Errore connessione:", err)
        return None