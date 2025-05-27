from patterns.builder.house.builder import Builder


class WoodenVillaBuilder(Builder):
    def build_floor(self):
        self._house.add("floor", "wood")

    def build_walls(self):
        self._house.add("walls", "wood panels")

    def build_door(self):
        self._house.add("door", "oak wood")

    def build_window(self):
        self._house.add("window", "glass with wooden frame")

    def build_pool(self):
        self._house.add("pool", "small garden pool")
