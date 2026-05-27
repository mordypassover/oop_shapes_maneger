from shape import Shape


class Rectangle(Shape):
    def __init__(self, shape_type = "rectangle"):
        super().__init__(shape_type)
        self.length, self.width = self.get_shape_param_s()

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return (self.length * 2) + (self.width * 2)

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.shape_type,
            "length": self.length,
            "width": self.width
            }

    def get_shape_param_s(self):
        return (int(input("enter length: ")),
                int(input("enter width:")))
