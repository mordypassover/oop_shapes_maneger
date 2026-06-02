import shape_manager
from fastapi import FastAPI, Response
from pydantic import BaseModel
import uvicorn


app = FastAPI()
SHAPE_MANAGER = shape_manager.ShapeManager()

class ShapeCreate(BaseModel):
    shape_name:str
    param_s:str

class UpdateShape(BaseModel):
    param_s :str


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


@app.post("/shapes/",status_code=201)
async def add_shape(user_data:ShapeCreate):
    shape_str = user_data.shape_name
    param_s_str = user_data.param_s
    SHAPE_MANAGER.create_shape(shape_str,tuple(param_s_str.split()))
    SHAPE_MANAGER.save_to_json()


@app.put("/shapes/{shape_id}")
def update_shape(shape_id:int,user_data:UpdateShape):
    param_s_str = user_data.param_s
    if shape_id in [shape.to_dict()["id"] for shape in SHAPE_MANAGER.shapes]:
        SHAPE_MANAGER.update_shape(shape_id, tuple(param_s_str.split()))
        SHAPE_MANAGER.save_to_json()
    else:
        Response.status_code = 404


@app.delete("/shapes/{shape_id}",status_code=200)
def remove_shape(shape_id:int):
    if shape_id in [shape.to_dict()["id"] for shape in SHAPE_MANAGER.shapes]:
        SHAPE_MANAGER.delete_shape(shape_id)
        SHAPE_MANAGER.save_to_json()
    else:
        Response.status_code = 404
