from patterns.factory.localizer.base import LocalizerFactory
from patterns.factory.localizer.localizers.english import EnglishLocalizer


class EnglishLocalizerFactory(LocalizerFactory):
    def create_localizer(self):
        return EnglishLocalizer()
