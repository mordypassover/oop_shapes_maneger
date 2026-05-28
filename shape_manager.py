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
            if instance.get_id() == shape_id :
                self.delete_shape(shape_id)
                self.create_shape(instance.shape_type, new_data,shape_id = shape_id)
                return
        logger.warning(f"object with id - {shape_id} not found")


    def delete_shape(self, shape_id):
        instance_list = self.get_all_shapes()
        for instance in instance_list:
            if instance.get_id() == shape_id :
                instance_list.remove(instance)
                return
        logger.warning(f"object with id - {shape_id} not found")


    def save_to_json(self):
        json_loadable_list = [shape_inst.__dict__ for shape_inst in self.shapes]
        with open("shapes.json", "w", encoding="utf-8") as file:
            json.dump(json_loadable_list, file, ensure_ascii=False, indent=4)


    def load_from_json(self):
        if  os.path.getsize("shapes.json") == 0:
            logger.info("shapes.json is empty or does not exist. Starting fresh.")
            return

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

    sm.save_to_json()

    sm2 = ShapeManager()
    sm2.load_from_json()
    sm2.create_shape("circle", (2,))
    sm2.create_shape("square", (3,))
    sm2.create_shape("rectangle", (4, 5))
    print(sm2.get_all_shapes())
    print(sm2.get_all_shapes()[5].shape_id)
    print(sm2.get_all_shapes()[4].shape_type)

    sm2.save_to_json()


