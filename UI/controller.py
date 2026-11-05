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
    def popola_biblioteca_dropdown(self):
        elenco_biblioteche = self._model.get_biblioteche()
        return [ft.DropdownOption(key=biblioteca['id'], text = biblioteca['nome']) for biblioteca in elenco_biblioteche]

    def popola_genere_dropdown(self):
        elenco_generi = self._model.get_generi()
        return [ft.DropdownOption(key=genere, text=genere) for genere in elenco_generi]

    # CALLBACKS DROPDOWN
    # TODO

    # AZIONE: MOSTRA LIBRI
    # TODO
    def cerca(self, e):
        self._view.messaggioDiErrore.visible = False
        biblioteca = self._view.selettoreBiblioteca.value
        genere = self._view.selettoreGenere.value
        libri = self._model.get_libri_filtrati(biblioteca, genere) #lista di oggetti
        if libri is None : self._view.messaggioDiErrore.visible = True
        if libri is not None: self._view.elencoLibri.controls = [ft.Text(str(el)) for el in libri]
        self._view.update()
