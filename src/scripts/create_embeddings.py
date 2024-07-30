from sentence_transformers import SentenceTransformer
import json
import pandas as pd
import os

model = SentenceTransformer("BAAI/bge-small-en-v1.5")

with open('src/data/bookmarks.json', 'r') as f:
   data = json.load(f)

def generate_embeddings(text):
  embedding = model.encode(text)
  return embedding.tolist()


df = pd.DataFrame(data)

df['embeddings'] = df['tweetContent'].apply(generate_embeddings)

directory = "src/data/embeds"
os.makedirs(directory, exist_ok=True)
df.to_csv(os.path.join(directory,'embeddings.csv'), index=False)
print("embeddings created...")
