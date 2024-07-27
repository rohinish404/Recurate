from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import lancedb
from src.scripts.create_lancedb_database import EmbeddingModel
from src.scripts.create_lancedb_image_table import TwtImgs
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

db = lancedb.connect('embeds/')
table = db.open_table("Embeddings")

db_img = lancedb.connect('lancedb_imgs')
table_img = db_img.open_table("imgs")

class Ask(BaseModel):
    query:str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/get_twt_results")
async def get_twt_results(request: Ask):
    actual = table.search(request.query, query_type="hybrid").limit(10).to_pydantic(EmbeddingModel)
    return actual

@app.post("/get_img_results")
async def get_img_results(request: Ask):
    rs = table_img.search(request.query).limit(3).to_pydantic(TwtImgs)
    return rs

