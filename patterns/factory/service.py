from patterns.factory.localizer.factories.english_factory import \
    EnglishLocalizerFactory
from patterns.factory.localizer.factories.french_factory import \
    FrenchLocalizerFactory
from patterns.factory.localizer.factories.spanish_factory import \
    SpanishLocalizerFactory


class Localize:
    def get(self):
        f = FrenchLocalizerFactory()
        e = EnglishLocalizerFactory()
        s = SpanishLocalizerFactory()

        message = ["car", "bike", "cycle"]

        for msg in message:
            # Create and use localizers without knowing the concrete classes
            # print(f.create_localizer().localize(msg))
            # print(e.create_localizer().localize(msg))
            # print(s.create_localizer().localize(msg))

            print(f.create_localizer().get_code())
            print(e.create_localizer().get_code())
            print(s.create_localizer().get_code())
