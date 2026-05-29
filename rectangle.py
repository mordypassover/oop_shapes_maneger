from shape import Shape


class Rectangle(Shape):
    def __init__(self, param_s,shape_id , shape_type = "rectangle"):
        super().__init__(shape_type, shape_id)
        self.length_width = tuple(int(param) for param in param_s)

    def get_area(self):
        return self.length_width[0] * self.length_width[1]

    def get_perimeter(self):
        return (self.length_width[0] * 2) + (self.length_width[1] * 2)

    def to_dict(self):
        return {
            "id": self.shape_id,
            "type": self.shape_type,
            "length": self.length_width[0],
            "width": self.length_width[1]
            }