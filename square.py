from shape import Shape


class Square(Shape):
    def __init__(self, parsam_s, shape_type = "square"):
        super().__init__(shape_type)
        self.side = parsam_s[0]


    def get_area(self):
        return self.side * self.side

    def get_perimeter(self):
        return self.side * 4

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.shape_type,
            "side": self.side
            }