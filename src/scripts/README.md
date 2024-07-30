# Scripts

A bunch of python scripts needed for running the app. 

- `classify_tweets.py`  - categorizes the tweets into 4 labels(for now) i.e. computer science, math, physics and others. Uses llama3 70b from groq for classification.
- `create_embeddings.py` - creates embeddings of content in every tweet and saves them to a csv file. Model used - BAAI/bge-small-en-v1.5.
- `create_lancedb_database` - creates a lancedb database of tweets as well as their embeddings for semantic search.
- `create_lancedb_image_table` - creates lancedb database for images and their embeddings for image search aka memeSearch. open-clip used for embeddings.
- `preprocessing.py` - preprocesses the data if neede anywhere. such as no empty fields in image_data json file.
- `url_to_imgs.py` - after scraping, we get the links to imgs but for lancedb image database we need all the images downloaded. this script downloads every image to a dir i.e. `src/data/downloaded_images/

## How to use?

You don't need to run these scripts one by one. It is already handeled by the `execute.sh` file in the root dir.
