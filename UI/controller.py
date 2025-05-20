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
        anno = self._view.ddyear.value
        nazione = self._view.ddcountry.value
        if nazione is None:
            self._view.create_alert("Devi inserire una nazione")
            return
        if anno is None:
            self._view.create_alert("Devi inserire un anno")
            return
        self._model.buildGraph(anno, nazione)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {self._model.getNumNodi()} Numero di Archi: {self._model.getNumArchi()}"))
        self._view.update_page()

    def handle_volume(self, e):
        volumi = self._model.getVolumiVendita()
        self._view.txtOut2.controls.clear()
        for (retailer, volume) in volumi:
            self._view.txtOut2.controls.append(ft.Text(f"{retailer} --> {volume}"))
        self._view.update_page()

    def handle_path(self, e):
        pass
