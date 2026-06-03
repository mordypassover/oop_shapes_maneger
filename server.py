import shape_manager
from fastapi import FastAPI, Response ,HTTPException
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


@app.get("/shapes/total-area")
def get_all_shapes_area_sum():
    area =SHAPE_MANAGER.get_all_shapes_area_sum()
    return {"shape area": area}


@app.get("/shapes/count")
def get_shape_list_len():
    return {"number of shapes":len(SHAPE_MANAGER.shapes)}


@app.get("/shapes/type/{shape_type}")
def get_class_insts(shape_type):
    try:
        wanted =SHAPE_MANAGER.shape_search(shape_type)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=e)
    return wanted


@app.get("/shapes/{shape_id}", status_code=200)
def get_1_shape_by_id(shape_id : int,  response: Response):
    try:
        shape = SHAPE_MANAGER.get_single_shape(shape_id)
        return shape
    except IndexError as e:
        raise HTTPException(status_code=404, detail={"error" : e})


@app.post("/shapes/",status_code=201)
async def add_shape(user_data:ShapeCreate):
    shape_str = user_data.shape_name
    param_s_str = user_data.param_s
    SHAPE_MANAGER.create_shape(shape_str,tuple(param_s_str.split()))
    SHAPE_MANAGER.save_to_json()


@app.put("/shapes/{shape_id}")
def update_shape(shape_id:int,user_data:UpdateShape):
    param_s_str = user_data.param_s

    if shape_id not in [shape["id"] for shape in SHAPE_MANAGER.show_shapes_as_dicts()]:
        raise HTTPException(status_code = 404, detail={"error" :f"shape id {shape_id} not found"})

    SHAPE_MANAGER.update_shape(shape_id, tuple(param_s_str.split()))
    SHAPE_MANAGER.save_to_json()


@app.delete("/shapes/{shape_id}",status_code=200)
def remove_shape(shape_id:int):
    if shape_id not in [shape["id"] for shape in SHAPE_MANAGER.show_shapes_as_dicts()]:
        raise HTTPException(status_code=404, detail={"error" :f"shape id {shape_id} not found"})

    SHAPE_MANAGER.delete_shape(shape_id)
    SHAPE_MANAGER.save_to_json()

