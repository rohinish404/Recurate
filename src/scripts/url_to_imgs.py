import json
import os
import requests
from urllib.parse import urlparse

def download_images(json_file, output_dir):
    result = []
    os.makedirs(output_dir, exist_ok=True)

    with open(json_file, 'r') as f:
        data = json.load(f)

    for i, dat in enumerate(data):
        try:
            url = dat["media"][0]
            response = requests.get(url, stream=True)
            response.raise_for_status()
            result.append({"image_links": dat["media"][0]})

            file_name = f'image_{i}.jpg'

            file_path = os.path.join(output_dir, file_name)

            with open(file_path, 'wb') as img_file:
                for chunk in response.iter_content(chunk_size=8192):
                    img_file.write(chunk)

            print(f"Downloaded: {file_path}")

        except Exception as e:
            print(f"Error downloading {url}: {str(e)}")
    with open("src/data/image_links.json",'w') as f:
        json.dump(result,f,indent=2)

if __name__ == "__main__":
    json_file = "src/data/Image_data.json"  
    output_dir = "src/data/downloaded_images"
    download_images(json_file, output_dir)
    print(f"All images downloaded to {output_dir}")
