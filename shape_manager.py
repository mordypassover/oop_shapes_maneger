import json
from square import Square
from circle import Circle
from rectangle import Rectangle


class ShapeManager:
    def __init__(self):
        self.shapes = []
       # self.load_from_json()

    def create_shape(self, shape):
        shape_dict = {"square" : Square, "circle" : Circle, "rectangle" : Rectangle}
        if shape in shape_dict:
            self.shapes.append(shape_dict[shape]().to_dict())

    def get_all_shapes(self):
        pass
    def update_shape(self, shape_id, new_data):
        pass
    def delete_shape(self, shape_id):
        pass
    def save_to_json(self):
        pass
    def load_from_json(self):
        with open("shapes.json", "r", encoding="utf-8") as f:
            return json.load(f)
