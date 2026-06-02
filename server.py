import shape_manager
from fastapi import FastAPI
import uvicorn


app = FastAPI()
SHAPE_MANAGER = shape_manager.ShapeManager()
