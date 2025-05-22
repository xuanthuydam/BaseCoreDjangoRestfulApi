from patterns.factory.localizer.base import LocalizerFactory
from patterns.factory.localizer.localizers.french import FrenchLocalizer


class FrenchLocalizerFactory(LocalizerFactory):
    def create_localizer(self):
        return FrenchLocalizer()
