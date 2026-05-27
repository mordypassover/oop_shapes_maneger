from math import pi
from shape import Shape


class Circle(Shape):

    def __init__(self, shape_type = "circle"):
        super().__init__(shape_type)
        self.radius = self.get_shape_param_s()


    def get_area(self):
        return self.radius ** 2 * pi

    def get_perimeter(self):
        return self.radius * 2 * pi

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.shape_type,
            "radius": self.radius
            }
    def get_shape_param_s(self):
        return int(input("get radius: "))
