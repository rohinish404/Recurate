import json

def filter_json_data(input_file, output_file):

    with open(input_file, 'r') as f:
        data = json.load(f)


    filtered_data = [dat for dat in data if dat["media"][0] is not None]


    with open(output_file, 'w') as f:
        json.dump(filtered_data, f, indent=2)

    items_removed = len(data) - len(filtered_data)
    print(f"Number of items removed: {items_removed}")

    return filtered_data


input_file = 'src/data/image_data.json'  
output_file = 'src/data/Image_data.json' 

filtered_data = filter_json_data(input_file, output_file)
print("data preprocessed...")
