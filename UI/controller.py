import flet as ft
from UI.view import View
from database import biblioteca_DAO
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO
    def popola_biblioteca_dropdown(self, genere = None):
        elenco_biblioteche = self._model.get_biblioteche(genere)
        result = [ft.DropdownOption(key="0", text="Qualunque")]
        for biblioteca in elenco_biblioteche:
            result.append(ft.DropdownOption(key=biblioteca['id'], text = biblioteca['nome']))
        return result

    def popola_genere_dropdown(self, id_biblioteca = None):
        elenco_generi = self._model.get_generi(id_biblioteca)
        result = [ft.DropdownOption(key = "0", text = "Qualunque")]
        for genere in elenco_generi:
            result.append(ft.DropdownOption(key=genere, text=genere))
        return result

    # CALLBACKS DROPDOWN
    # TODO
    def nuova_lista_genere(self, e):
        id_biblioteca = self._view.selettoreBiblioteca.value
        if id_biblioteca == "0": id_biblioteca = None
        self._view.selettoreGenere.options = self.popola_genere_dropdown(id_biblioteca)

    def nuova_lista_biblioteca(self, e):
        genere = self._view.selettoreGenere.value
        if genere == "0": genere = None
        self._view.selettoreBiblioteca.options = self.popola_biblioteca_dropdown(genere)

    # AZIONE: MOSTRA LIBRI
    # TODO
    def cerca(self, e):
        self._view.messaggioDiErrore.visible = False
        biblioteca = self._view.selettoreBiblioteca.value
        genere = self._view.selettoreGenere.value
        if biblioteca == "0": biblioteca = None
        if genere == "0": genere = None
        print(biblioteca, genere)
        libri = self._model.get_libri_filtrati(biblioteca, genere) #lista di oggetti
        if libri is None : self._view.messaggioDiErrore.visible = True
        if libri is not None: self._view.elencoLibri.controls = [ft.Text(str(el)) for el in libri]
        self._view.update()
