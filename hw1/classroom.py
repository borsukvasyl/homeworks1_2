class Classroom():
    """
    Represents a classroom in an academic building.
    """
    def __init__(self, number, capacity, equipment):
        self.number = number
        self.capacity = capacity
        self.equipment = equipment

    def is_larger(self, classroom):
        """
        object -> bool

        Checks whether current classroom has bigger capacity then other.
        """
        if self.capacity > classroom.capacity:
            return True
        return False

    def equipment_differences(self, classroom):
        """
        object -> list(str)

        Finds all equipment that isn`t in another classroom.
        """
        differences = []
        for equipment in self.equipment:
            if equipment not in classroom.equipment:
                differences.append(equipment)
        return differences

    def __str__(self):
        equipment = ""
        for element in self.equipment:
            equipment += element + ", "
        return "Classroom " + self.number + " has a capacity of " + str(self.capacity) +\
               " persons and has the following equipment: " + equipment[:-2] + "."

    def __repr__(self):
        return "Classroom('" + self.number + "', " + str(self.capacity) + ", " + str(self.equipment) + ")"
