from abc import ABC, abstractmethod, ABCMeta


class Figure(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        pass
