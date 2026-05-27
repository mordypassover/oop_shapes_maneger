import json
import logging
from square import Square
from circle import Circle
from rectangle import Rectangle


logging.basicConfig(level=logging.INFO, format='%(levelname)s | %(message)s  | %(asctime)s', encoding="utf-8")
logger = logging.getLogger(__name__)


class ShapeManager:
    def __init__(self):
        self.shapes = []
        # self.load_from_json()

    def create_shape(self, shape):
        logging.info("started to create a shape")
        shape_dict = {"square" : Square, "circle" : Circle, "rectangle" : Rectangle}
        if shape in shape_dict:
            try:
                self.shapes.append( shape_dict[shape]())
            except ValueError :
                logging.error("input not valid!")
            logging.info("finished to create shape")
        else:
            logging.error(f"shape -{shape} not supported")
    def get_all_shapes(self):
        return self.shapes

    def update_shape(self, shape_id, new_data):
        pass
    def delete_shape(self, shape_id):
        pass
    def save_to_json(self):
        pass
    def load_from_json(self):
        with open("shapes.json", "r", encoding="utf-8") as f:
            return json.load(f)

if __name__ == "__main__":
    sm = ShapeManager()
    sm.create_shape("square")
    print(sm.shapes )
