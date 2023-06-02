import abc
class Imposto(abc.ABC):
    @abc.abstractmethod
    def imposto(self):
        pass