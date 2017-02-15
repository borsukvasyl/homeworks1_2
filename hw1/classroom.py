class Classroom():
    def __init__(self, number, capacity, equipment):
        self.number = number
        self.capacity = capacity
        self.equipment = equipment

    def is_larger(self, classroom):
        if self.capacity > classroom.capacity:
            return True
        return False

    def equipment_differences(self, classroom):
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


classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
classroom_007 = Classroom('007', 12, ['TV'])
print(classroom_016.is_larger(classroom_007))
print(classroom_016.equipment_differences(classroom_007))
print([classroom_016])
