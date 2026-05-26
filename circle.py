from math import pi

from shape import Shape


class Circle(Shape):
    def __init__(self, shape_id, shape_type, radius):
        super().__init__(shape_id, shape_type)
        self.radius = radius


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
