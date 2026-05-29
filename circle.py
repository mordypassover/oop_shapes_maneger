from math import pi
from shape import Shape


class Circle(Shape):

    def __init__(self, param_s, shape_id, shape_type = "circle"):
        super().__init__(shape_type, shape_id)
        self.radius = int(param_s[0])


    def get_area(self):
        return self.radius ** 2 * pi

    def get_perimeter(self):
        return self.radius * 2 * pi

    def to_dict(self):
        return {
            "id": self.shape_id,
            "type": self.shape_type,
            "radius": self.radius
            }