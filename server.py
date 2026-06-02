import shape_manager
from fastapi import FastAPI
import uvicorn


app = FastAPI()
SHAPE_MANAGER = shape_manager.ShapeManager()


@app.get("/shapes")
def get_all_shapes_as_dicts():
    return SHAPE_MANAGER.show_shapes_as_dicts()

