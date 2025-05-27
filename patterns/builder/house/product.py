class House:
    def __init__(self):
        self.structure = {}

    def add(self, part: str, value: str):
        self.structure[part] = value

    def describe(self):
        for part, material in self.structure.items():
            print(f"{part.capitalize()}: {material}")
