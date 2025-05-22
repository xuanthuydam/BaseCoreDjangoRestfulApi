from patterns.factory.localizer.base import Localizer


class SpanishLocalizer(Localizer):
    def __init__(self):
        self.translations = {
            "car": "coche",
            "bike": "bicicleta",
            "cycle": "ciclo",
        }

    def localize(self, msg):
        return self.translations.get(msg, msg)

    def get_code(self):
        return "SP"
