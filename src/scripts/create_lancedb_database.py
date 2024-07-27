import lancedb
from lancedb.pydantic import LanceModel, Vector
from lancedb.embeddings import get_registry
import pandas as pd
import numpy as np
model = get_registry().get("sentence-transformers").create(name="BAAI/bge-small-en-v1.5", device="cpu")

class EmbeddingModel(LanceModel):
    tweetContent: str = model.SourceField()
    embeddings : Vector(model.ndims()) = model.VectorField()
    username: str

embeds_df = pd.read_csv("src/data/embeds/embeddings.csv")
embeds_df['embeddings'] = embeds_df['embeddings'].apply(lambda x: np.fromstring(x.strip("[]"), sep=','))
db = lancedb.connect("embeds/")
table = db.create_table("Embeddings", data= embeds_df,schema=EmbeddingModel, mode="overwrite")

table.create_fts_index("tweetContent", replace=True)

print("Table Created.")
