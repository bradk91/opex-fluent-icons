import os
import json

cwd = os.getcwd()
asset_dir = os.path.join(cwd, 'assets')

all_icons = []
this_icon = {}
i = 0

# Go through the assets directory and get each metadata.json file, add to the manifest
for root, dirs, files in os.walk(asset_dir):
    if 'metadata.json' in files:
        metadata_path = os.path.join(root, 'metadata.json')
        this_icon = {}
        with open(metadata_path, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
            all_icons.append(metadata)


print(all_icons[1])
