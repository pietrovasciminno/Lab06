import flet as ft
from UI.view import View
from modell.model import Autonoleggio

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view : View, model : Autonoleggio):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    def get_elenco_automobili(self, e):
        self._view.lista_auto.controls.clear()
        lista = self._model.get_automobili()
        if lista is not None:
            if len(lista) > 0 :
                for  auto in lista:
                    stato = "✅" if auto.disponibile else "⛔"
                    self._view.lista_auto.controls.append(ft.Text(f"{stato} {auto}"))
                self._view.update()
            else:
                self._view.show_alert("❌ Non ci sono auto nel database")
        else:
            self._view.show_alert("❌ Non è stato possibile connettersi")

    def cerca_automobili(self,e):
        self._view.lista_auto_ricerca.controls.clear()
        lista_ricerca = self._model.cerca_automobili_per_modello()
        if lista_ricerca is not None:
            if len(lista_ricerca) > 0 :
                for auto in lista_ricerca:
                    stato = "✅" if auto.disponibile else "⛔"
                    self._view.lista_auto_ricerca.controls.append(ft.Text(f"{stato} {auto}"))
                self._view.update()
            else:
                self._view.show_alert("❌ Nessuna auto trovata")
        else:
            self._view.show_alert("❌ Non è stato possibile connettersi")
