from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # TODO
    def get_genre(self):
        self.cnx = DBConnect.get_connection()  # dovrebbe restituire l'equivalente di mysql.connector.connect
        cursore = self.cnx.cursor(dictionary=True)  # creazione cursore
        query = ("""SELECT DISTINCT(genere)
                    FROM libro""")
        cursore.execute(query)
        # lista_generi = cursore.fetchall()
        lista_generi = [el['genere'] for el in cursore.fetchall()]
        cursore.close()
        self.cnx.close()
        return lista_generi #return ['fantasy','poesia','giallo']


    def get_books(self, biblioteca, genere):
        self.cnx = DBConnect.get_connection()  # dovrebbe restituire l'equivalente di mysql.connector.connect
        cursore = self.cnx.cursor(dictionary=True)  # creazione cursore
        query = (f"""SELECT *
                    FROM libro
                    WHERE id_biblioteca = {biblioteca} AND genere = '{genere}'""")
        cursore.execute(query)
        lista_libri = []
        for libro in cursore.fetchall():
            lista_libri.append(Libro(**libro))
        cursore.close()
        self.cnx.close()
        return lista_libri
