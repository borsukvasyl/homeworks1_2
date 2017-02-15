class Building():
    """
    Represents a building.
    """
    def __init__(self, address):
        self.address = address


class House(Building):
    """
    Represents a house with apartments.
    """
    def __init__(self, address, apartments):
        super().__init__(address)
        self.apartments = apartments
