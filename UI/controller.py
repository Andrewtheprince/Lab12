import flet as ft


class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

        self._listYear = []
        self._listCountry = []

    def fillDD(self):
        nazioni = self._model.getNazioni()
        for nazione in nazioni:
            self._view.ddcountry.options.append(ft.dropdown.Option(nazione))
            self._listCountry.append(nazione)
        self._listYear.extend([2015,2016,2017,2018])
        for anno in self._listYear:
            self._view.ddyear.options.append(ft.dropdown.Option(anno))

    def handle_graph(self, e):
        pass

    def handle_volume(self, e):
        pass

    def handle_path(self, e):
        pass
