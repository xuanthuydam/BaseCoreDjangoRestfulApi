from abc import ABC, abstractmethod

from patterns.builder.house.product import House


class Builder(ABC):
    def __init__(self):
        self.reset()

    def reset(self):
        self._house = House()

    @property
    def house(self) -> House:
        house = self._house
        self.reset()
        return house

    @abstractmethod
    def build_floor(self):
        pass

    @abstractmethod
    def build_walls(self):
        pass

    @abstractmethod
    def build_door(self):
        pass

    @abstractmethod
    def build_window(self):
        pass

    def build_garage(self):
        pass

    def build_pool(self):
        pass
