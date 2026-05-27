class Shape:
    counter = 0
    def __init__(self, shape_type):
        self.id = Shape.counter
        self.shape_type = shape_type
        Shape.counter += 1

    def get_area(self):
        pass
    def get_perimeter(self):
        pass
    def to_dict(self):
        pass
    def get_shape_id(self):
        return self.id
    def get_shape_param_s(self):
        pass