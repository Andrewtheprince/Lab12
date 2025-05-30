import networkx as nx
from database.DAO import DAO

class Model:

    def __init__(self):
        self._graph = nx.Graph()
        self._idMapRetailer = {}

    @staticmethod
    def getNazioni():
        return DAO.getAllNazioni()

    def buildGraph(self, anno, nazione):
        self._graph.clear()
        self._idMapRetailer.clear()
        retailers = DAO.getRetailers(nazione)
        for retailer in retailers:
            self._idMapRetailer[retailer.Retailer_code] = retailer
        self._graph.add_nodes_from(retailers)
        archi = DAO.getArchi(anno)
        for arco in archi:
            if arco["retailer1"] in self._idMapRetailer and arco["retailer2"] in self._idMapRetailer:
                self._graph.add_edge(self._idMapRetailer[arco["retailer1"]], self._idMapRetailer[arco["retailer2"]], weight = arco["tot"])

    def getNumNodi(self):
        return len(self._graph.nodes)

    def getNumArchi(self):
        return len(self._graph.edges)

    def getVolumiVendita(self):
        somme_pesi = [(nodo, sum(d['weight'] for _,_, d in self._graph.edges(nodo, data=True))) for nodo in self._graph.nodes()]
        somme_pesi_ordinate = sorted(somme_pesi, key=lambda x: x[1], reverse=True)
        return somme_pesi_ordinate