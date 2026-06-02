from requests import Response

import shape_manager
from fastapi import FastAPI, Response
import uvicorn


app = FastAPI()
SHAPE_MANAGER = shape_manager.ShapeManager()


@app.get("/shapes")
def get_all_shapes_as_dicts():
    return SHAPE_MANAGER.show_shapes_as_dicts()


@app.get("/shapes/{id}", status_code=200)
def get_1_shape_by_id(id : int,  response: Response):
    all_shapes = SHAPE_MANAGER.show_shapes_as_dicts()
    for shape in all_shapes:
        if int(id) == shape["id"]:
            return shape
    response.status_code = 404
    return {"status" : "shape id not found"}