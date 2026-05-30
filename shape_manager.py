import json
import os
import logging
from square import Square
from circle import Circle
from rectangle import Rectangle



logging.basicConfig(level=logging.INFO, format='%(levelname)s | %(message)s  | %(asctime)s', encoding="utf-8")
logger = logging.getLogger(__name__)


class ShapeManager:
    def __init__(self):
        self.shapes = []
        self.load_from_json()

    def create_shape(self, shape: str, param_s: tuple, forced_id=None):
        logging.info("started to create a shape")

        new_id = forced_id if forced_id is not None else self.get_id()
        shape_dict = {"square": Square, "circle": Circle, "rectangle": Rectangle}
        if shape in shape_dict:
            try:
                self.shapes.append(shape_dict[shape](param_s, shape_id=new_id))
            except ValueError as e:
                logging.error(f"input not valid!,{e}")

            logging.info("finished to create shape")
        else:
            logging.error(f"shape - {shape} not supported")


    def get_all_shapes(self):
        logger.info("getting all shapes from list")
        self.sort_shapes()
        return self.shapes

    def show_shapes_as_dicts(self):
        logger.info("getting all shapes dicts")
        if not self.shapes:
            return "no shapes in list"
        return [shape.to_dict() for shape in self.get_all_shapes()]


    def update_shape(self, shape_id, new_data):
        logger.info(f"running update shape, for shape id {shape_id}")
        for instance in self.get_all_shapes():
            if instance.get_shape_id() == shape_id :
                self.delete_shape(shape_id)
                self.create_shape(instance.shape_type, new_data, forced_id=shape_id)
                logger.info(f"updated id {shape_id} successfully")
                return
        logger.warning(f"object with id - {shape_id} not found")


    def delete_shape(self, shape_id):
        logger.info(f"running delete shape, for shape id {shape_id}")
        instance_list = self.get_all_shapes()
        for instance in instance_list:
            if instance.get_shape_id() == shape_id :
                instance_list.remove(instance)
                logger.info(f"deleted id {shape_id} successfully")
                return
        logger.warning(f"object with id - {shape_id} not found")


    def save_to_json(self):
        logger.info("uploading all shapes to json")
        json_loadable_list = [shape.to_dict() for shape in self.shapes]
        with open("shapes.json", "w", encoding="utf-8") as file:
            json.dump(json_loadable_list, file, ensure_ascii=False, indent=4)


    def load_from_json(self):
        if  os.path.getsize("shapes.json") == 0:
            logger.info("shapes.json is empty  Starting fresh")
            return

        with open("shapes.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            for item in data:
                shape_type = item.get('type')
                if shape_type == "circle":
                    params = (item.get('radius'),)
                elif shape_type == "square":
                    params = (item.get('side'),)
                elif shape_type == "rectangle":
                    params = (item.get("length"), item.get('width'))
                else:
                    logger.warning("shape not suported")


                self.create_shape(shape_type, params, forced_id=item.get("id"))

        logger.info(f"successfully loaded {len(data)} shapes from json ")


    def get_id(self):
        logger.info("started looking for id")
        new_id =  1 if not self.shapes else (max(shape.shape_id for shape in self.shapes) +1)
        logger.info("got new id")
        return new_id

    def sort_shapes(self):
        self.shapes.sort(key=lambda shape: shape.shape_id)

if __name__ == "__main__":
    sm = ShapeManager()
    sm.create_shape("circle",(2,))
    sm.create_shape("square", (3,))
    sm.create_shape("rectangle",(4, 5))
    print(sm.get_all_shapes() )
    print(sm.get_all_shapes()[1].shape_id)
    print(sm.get_all_shapes()[2].shape_type)
    sm.update_shape(2, (2,))
    sm.delete_shape(3)
    print(sm.show_shapes_as_dicts())

    sm.save_to_json()

