from lancedb.embeddings import EmbeddingFunctionRegistry
import lancedb
from PIL import Image
from lancedb.pydantic import LanceModel, Vector
import pandas as pd
from pathlib import Path
from random import sample


registry = EmbeddingFunctionRegistry.get_instance()
clip = registry.get("open-clip").create()

class TwtImgs(LanceModel):
    vector: Vector(clip.ndims()) = clip.VectorField()
    image_uri: str = clip.SourceField()

    @property
    def image(self):
        return Image.open(self.image_uri)


db = lancedb.connect("lancedb_imgs")

if "imgs" in db:
    table = db["imgs"]
else:
    table = db.create_table("imgs", schema=TwtImgs)
    p = Path("src/data/downloaded_images")
    uris = [str(f) for f in p.glob("*.jpg")]
    uris = sample(uris, len(uris))
    table.add(pd.DataFrame({"image_uri": uris}))

print("Table created")
print(f"Tabel Info {table.to_pandas().info()}")
