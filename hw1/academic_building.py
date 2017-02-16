import classroom
from building import Building


class AcademicBuilding(Building):
    """
    Represents a academic building with classrooms.
    """
    def __init__(self, address, classrooms):
        super().__init__(address)
        self.classrooms = classrooms

    def total_equipment(self):
        """
        None -> list(tuple(str, int))

        Counts every equipment.
        """
        equipment = [element for i in range(len(self.classrooms)) for element in self.classrooms[i].equipment]
        total_equipment = []
        for element in set(equipment):
            total_equipment.append((element, equipment.count(element)))
        return total_equipment

    def __str__(self):
        string = self.address
        for classroom in self.classrooms:
            string += "\n" + str(classroom)
        return string
