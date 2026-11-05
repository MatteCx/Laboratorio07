from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # TODO

    def get_biblioteca(self):
        self.cnx = DBConnect.get_connection()  # dovrebbe restituire l'equivalente di mysql.connector.connect
        cursore = self.cnx.cursor(dictionary=True)  # creazione cursore
        query = ("""SELECT id, nome
                    FROM biblioteca""")
        cursore.execute(query)
        lista_biblioteche = cursore.fetchall()
        cursore.close()
        self.cnx.close()
        return lista_biblioteche      #return [{'id': 1, 'nome': 'Biblioteca civica Italo Calvino'}, {'id': 2, 'nome': 'Biblioteca civica Francesco Cognasso'}, {'id': 3, 'nome': 'Biblioteca civica Cesare Pavese}]