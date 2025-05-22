from abc import ABC, abstractmethod


# Abstract Product
class Localizer(ABC):
    @abstractmethod
    def localize(self, msg):
        pass

    @abstractmethod
    def get_code(self):
        pass


# Abstract Factory
class LocalizerFactory(ABC):
    @abstractmethod
    def create_localizer(self) -> Localizer:
        pass
