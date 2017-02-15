import classroom


class AcademicBuilding():
    def __init__(self, address, classrooms):
        self.address = address
        self.classrooms = classrooms

    def total_equipment(self):
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


'''
classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
classroom_007 = classroom.Classroom('007', 12, ['TV'])
classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
classrooms = [classroom_016, classroom_007, classroom_008]
building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
print(building.total_equipment())
print(building)
'''