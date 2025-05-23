class Nodo:
    def __init__(self, chiave):
        self.chiave = chiave
        self.valori = [chiave]  # lista che contiene tutti i valori con questa chiave
        self.sinistro = None
        self.destro = None

class ABR:
    def __init__(self):
        self.radice = None

    def insert(self, chiave):
        self.radice = self._insert_ric(self.radice, chiave)

    def _insert_ric(self, nodo, chiave):
        if nodo is None:
            return Nodo(chiave)
        if chiave < nodo.chiave:
            nodo.sinistro = self._insert_ric(nodo.sinistro, chiave)
        elif chiave > nodo.chiave:
            nodo.destro = self._insert_ric(nodo.destro, chiave)
        else:
            nodo.valori.append(chiave)  # aggiunge il duplicato alla lista
        return nodo

    def cerca(self, chiave):
        return self._cerca_ric(self.radice, chiave)

    def _cerca_ric(self, nodo, chiave):
        if nodo is None:
            return False
        if chiave == nodo.chiave:
            return True
        elif chiave < nodo.chiave:
            return self._cerca_ric(nodo.sinistro, chiave)
        else:
            return self._cerca_ric(nodo.destro, chiave)

    def in_ordine(self):
        return self._in_ordine_ric(self.radice)

    def _in_ordine_ric(self, nodo):
        if nodo is None:
            return []
        return self._in_ordine_ric(nodo.sinistro) + [(nodo.chiave, len(nodo.valori))] + self._in_ordine_ric(nodo.destro)
