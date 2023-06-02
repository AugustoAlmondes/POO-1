import abc

class Tributo(abc.ABC):
    @abc.abstractmethod
    def tributo(self):
        pass