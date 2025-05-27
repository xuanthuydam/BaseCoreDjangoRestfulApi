from patterns.builder.house.concrete.house_with_garage import \
    HouseWithGarageBuilder
from patterns.builder.house.concrete.wooden_villa import WoodenVillaBuilder
from patterns.builder.house.director import Director


class BuilderService:
    def get(self):
        """
        Build a wooden villa and a concrete house with a garage.
        The director is used to build the houses.
        The builder is used to build the house.
        The house is a product of the builder.
        The director is used to build the house.
        The builder is used to build the house.
        """

        director = Director()

        print("🏡 Build wooden villa:")
        builder1 = WoodenVillaBuilder()
        director.set_builder(builder1)
        director.build_luxury_house()
        house1 = builder1.house
        house1.describe()

        print("\n🏠 Build house with garage:")
        builder2 = HouseWithGarageBuilder()
        director.set_builder(builder2)
        director.build_luxury_house()
        house2 = builder2.house
        house2.describe()
