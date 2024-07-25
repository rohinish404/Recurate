from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import lancedb
from create_lancedb_database import EmbeddingModel
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

class Ask(BaseModel):
    query:str

@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.post("/ask")
async def get_results(request: Ask):
    actual = table.search(request.query, query_type="hybrid").limit(10).to_pydantic(EmbeddingModel)
    return actual

