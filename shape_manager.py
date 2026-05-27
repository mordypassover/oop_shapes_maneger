import json
import logging
from square import Square
from circle import Circle
from rectangle import Rectangle
from shape import Shape


logging.basicConfig(level=logging.INFO, format='%(levelname)s | %(message)s  | %(asctime)s', encoding="utf-8")
logger = logging.getLogger(__name__)


class ShapeManager:
    def __init__(self):
        self.shapes = []
        # self.load_from_json()

    def create_shape(self, shape:str,  param_s:tuple ,shape_id = Shape.counter):
        logging.info("started to create a shape")
        shape_dict = {"square" : Square, "circle" : Circle, "rectangle" : Rectangle}
        if shape in shape_dict:
            try:
                self.shapes.append( shape_dict[shape](param_s))
            except ValueError :
                logging.error("input not valid!")
            logging.info("finished to create shape")
        else:
            logging.error(f"shape -{shape} not supported")
    def get_all_shapes(self):
        return self.shapes

    def update_shape(self, shape_id, new_data):
        for instance in self.get_all_shapes():
            if instance.id == shape_id :
                self.delete_shape(shape_id)
                self.create_shape(instance.shape_type, new_data,shape_id = shape_id)


    def delete_shape(self, shape_id):
        pass
    def save_to_json(self):
        pass
    def load_from_json(self):
        with open("shapes.json", "r", encoding="utf-8") as f:
            return json.load(f)

if __name__ == "__main__":
    sm = ShapeManager()
    sm.create_shape("circle",(2,))
    sm.create_shape("square", (3,))
    sm.create_shape("rectangle",(4, 5))
    print(sm.get_all_shapes() )
    print(sm.get_all_shapes()[1].id)
    print(sm.get_all_shapes()[2].shape_type)


