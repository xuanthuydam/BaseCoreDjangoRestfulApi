from patterns.factory.localizer.base import Localizer


class FrenchLocalizer(Localizer):
    def __init__(self):
        self.translations = {
            "car": "voiture",
            "bike": "bicyclette",
            "cycle": "cyclette",
        }

    def localize(self, msg):
        return self.translations.get(msg, msg)

    def get_code(self):
        return "FR"
