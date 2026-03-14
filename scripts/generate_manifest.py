import os
import json

cwd = os.getcwd()
asset_dir = os.path.join(cwd, 'assets')

all_icons = {}
this_icon = {}

# Go through the assets directory and get each metadata.json file, add to the manifest
for root, dirs, files in os.walk(asset_dir):
    if 'metadata.json' in files:
        metadata_path = os.path.join(root, 'metadata.json')
        this_icon = {}
        with open(metadata_path, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
            all_icons[metadata['name']] = metadata

# Write the manifest to a file
manifest_path = os.path.join(cwd, 'manifest.json')
with open(manifest_path, 'w', encoding='utf-8') as f:
    json.dump(all_icons, f, indent=2)