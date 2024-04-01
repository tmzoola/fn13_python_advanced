from collections import namedtuple

Employee = namedtuple("Employee", ['name', 'age', 'department'])


ishch1 = Employee("Murodjon", 26, "IT")

print(type(ishch1))



Point = namedtuple("Point", ["x", "y", "z"])

point1 = Point(4,5,6)
point2 = Point(7,8,9)


print(point1 + point1)

