class Seguro:
    def __init__(self,valor,total):
        self._valor = valor
        self._total = total

    @property
    def valor(self):
        return self._valor

    @property
    def total(self):
        return self._total

    def tributo(self):
        return self._valor * 0.02 + 10