class Shape:
    def __init__(self, shape_type, shape_id):
        self.shape_id = shape_id
        self.shape_type = shape_type


    def get_area(self):
        pass
    def get_perimeter(self):
        pass
    def to_dict(self):
        pass
    def get_shape_id(self):
        return self.shape_id
    def get_shape_param_s(self):
        pass