from patterns.factory.localizer.base import LocalizerFactory
from patterns.factory.localizer.localizers.spanish import SpanishLocalizer


class SpanishLocalizerFactory(LocalizerFactory):
    def create_localizer(self):
        return SpanishLocalizer()
