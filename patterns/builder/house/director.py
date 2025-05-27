from patterns.builder.house.builder import Builder


class Director:
    def __init__(self, builder: Builder = None):
        self._builder = builder

    def set_builder(self, builder: Builder):
        self._builder = builder

    def build_basic_house(self):
        self._builder.build_floor()
        self._builder.build_walls()
        self._builder.build_door()
        self._builder.build_window()

    def build_luxury_house(self):
        self.build_basic_house()
        self._builder.build_garage()
        self._builder.build_pool()
