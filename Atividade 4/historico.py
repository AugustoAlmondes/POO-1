import datetime

class Historico():
    def __init__(self):
        self._data_criacao = datetime.datetime.now()
        self._transacoes = []
        
    @property
    def data_criacao(self):
        return self._data_criacao
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def add_transacao(self, t):
        self._transacoes.append(t)

    def imprime_transacoes(self):
        print(f'Data de abertura: {self._data_criacao}')
        for t in self._transacoes:
            print(t)