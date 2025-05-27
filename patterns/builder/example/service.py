from patterns.builder.example.concrete_builder import ConcreteBuilder1
from patterns.builder.example.director import Director


class BuilderService:
    def get(self):
        """
        The client code creates a builder object, passes it to the director and then
        initiates the construction process. The end result is retrieved from the
        builder object.
        """

        director = Director()
        builder = ConcreteBuilder1()
        director.builder = builder

        print("Standard basic product: ")
        director.build_minimal_viable_product()
        builder.product.list_parts()

        print("\n")

        print("Standard full featured product: ")
        director.build_full_featured_product()
        builder.product.list_parts()

        print("\n")

        # Remember, the Builder pattern can be used without a Director class.
        print("Custom product: ")
        builder.produce_part_a()
        builder.produce_part_b()
        builder.product.list_parts()
