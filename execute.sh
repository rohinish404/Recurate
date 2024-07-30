#!/bin/bash

echo "preprocessing..."
python3 src/scripts/preprocessing.py

echo "creating embeddings of tweets..."
python3 src/scripts/create_embeddings.py

echo "labelling tweets..."
python3 src/scripts/classify_tweets.py src/data/bookmarks.json

echo "creating lancedb database of tweets..."
python3 src/scripts/create_lancedb_database.py

echo "donwloading images from links for memeSearch..."
python3 src/scripts/url_to_imgs.py 

echo "creating lancedb database for images..."
python3 src/scripts/create_lancedb_image_table.py
