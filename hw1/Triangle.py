import point


class Triangle():
    def __init__(self, point1, point2, point3):
        self.points = point1, point2, point3
        self.lines = [calculate_line(self.points[i], self.points[j]) for i in range(2) for j in range(i + 1, 3)]

    def is_triangle(self):
        if sum(self.lines) - max(self.lines) < max(self.lines):
            return False
        return True

    def perimeter(self):
        return sum(self.lines)

    def area(self):
        p = self.perimeter() / 2
        area = p
        for line in self.lines:
            area *= p - line
        return area ** 0.5


def calculate_line(point1, point2):
    return ((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2) ** 0.5


'''
triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(1,3))
print(triangle.lines)
print(triangle.area())
'''