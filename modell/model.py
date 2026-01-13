from database.DB_connect import get_connection
from modell.automobile import Automobile
from modell.noleggio import Noleggio

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:
        cnx = get_connection()
        result = []
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM automobile")
            for row  in cursor:
                result.append(Automobile(row["codice"], row["marca"], row["modello"], row["anno"], row["posti"], row["disponibile"]))
            cursor.close()
            cnx.close()
            return result
        else:
            print("No Connection")
            return None

    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        cnx = get_connection()
        result = []
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            query = """ SELECT * FROM automobile
                        WHERE  automobile.modello = %s"""
            cursor.execute(query, (modello,))
            for row in cursor:
                result.append(Automobile(row["codice"], row["marca"], row["modello"], row["anno"], row["posti"],
                                         row["disponibile"]))
            cursor.close()
            cnx.close()
            return result
        else:
            print("No Connection")
            return None




