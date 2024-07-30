from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import lancedb
from src.scripts.create_lancedb_database import EmbeddingModel
from src.scripts.create_lancedb_image_table import TwtImgs
from pydantic import BaseModel
import json

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

db = lancedb.connect('embeds')
table = db.open_table("Embeddings")

db_img = lancedb.connect('imgs')
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
    print(table_img.head())
    rs = table_img.search(request.query).limit(10).to_pydantic(TwtImgs)
    return rs

@app.post("/get_label_results")
async def get_label_results(request: Ask):
    with open('src/data/bookmarks_with_label.json','r') as f:
        data = json.load(f)
    print(request.query)
    if (request.query == 'computer_science'):
        result = [dat for dat in data if dat["label"]=="computer science"]
        return result
    elif (request.query == 'math'):
        result = [dat for dat in data if dat["label"]=="math"]
        return result
    elif (request.query == 'physics'):
        result = [dat for dat in data if dat["label"]=="physics"]
        return result
    else:
        result = [dat for dat in data if dat["label"]=="others"]
        return result

        



















