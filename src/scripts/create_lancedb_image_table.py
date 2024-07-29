from lancedb.embeddings import EmbeddingFunctionRegistry
import lancedb
from PIL import Image
from lancedb.pydantic import LanceModel, Vector
import pandas as pd
from pathlib import Path
from random import sample
import json
import re
registry = EmbeddingFunctionRegistry.get_instance()
clip = registry.get("open-clip").create()

class TwtImgs(LanceModel):
    vector: Vector(clip.ndims()) = clip.VectorField()
    image_uri: str = clip.SourceField()
    image_links: str

    @property
    def image(self):
        return Image.open(self.image_uri)


db = lancedb.connect("imgs")

with open("src/data/image_links.json", 'r') as f:
    data = json.load(f)

extractedValues = [dat["image_links"] for dat in data]

if "imgs" in db:
    table = db["imgs"]
else:
    table = db.create_table("imgs", schema=TwtImgs)
    p = Path("src/data/downloaded_images")
    uris = [str(f) for f in p.glob("*.jpg")]
    uris.sort(key=lambda x: int(re.search(r'image_(\d+)\.jpg', x).group(1)))
    print(uris)
    table.add(pd.DataFrame({"image_uri": uris,"image_links":extractedValues}))
    

print("Table created")
print(f"Tabel Info {table.to_pandas().info()}")
