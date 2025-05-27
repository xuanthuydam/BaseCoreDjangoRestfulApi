from patterns.builder.house.builder import Builder


class HouseWithGarageBuilder(Builder):
    def build_floor(self):
        self._house.add("floor", "concrete slab")

    def build_walls(self):
        self._house.add("walls", "brick and cement")

    def build_door(self):
        self._house.add("door", "steel door")

    def build_window(self):
        self._house.add("window", "aluminum frame")

    def build_garage(self):
        self._house.add("garage", "attached 2-car garage")
