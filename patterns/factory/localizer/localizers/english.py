from patterns.factory.localizer.base import Localizer


class EnglishLocalizer(Localizer):
    def localize(self, msg):
        return msg

    def get_code(self):
        return "EN"
