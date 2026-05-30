from shape import Shape


class Square(Shape):
    def __init__(self, param_s, shape_id, shape_type = "square"):
        super().__init__(shape_type, shape_id)
        if len(param_s) != 1:
            raise ValueError("square needs 1 param")
        self.side = int(param_s[0])


    def get_area(self):
        return self.side * self.side

    def get_perimeter(self):
        return self.side * 4

    def to_dict(self):
        return {
            "id": self.shape_id,
            "type": self.shape_type,
            "side": self.side
            }

