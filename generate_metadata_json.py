import os
import json

cwd = os.getcwd()
assets_dir = os.path.join(cwd, 'assets')

metadata = {}

def get_icon_details(icon_dir):
    sizes = []
    styles = []
    svg_dir = os.path.join(icon_dir, 'SVG')
    for entry in os.scandir(svg_dir):
        if entry.is_file() and entry.name.endswith('.svg'):
            # Extract the size from the filename, which is like some_words_20_filled.svg
            size = entry.name.split('_')[-2]
            if size not in sizes:
                sizes.append(size)
            # Extract the style from the filename
            style = entry.name.split('_')[-1].split('.')[0]
            if style not in styles:
                styles.append(style)
    return sizes, styles

for entry in os.scandir(assets_dir):
    if entry.is_dir():
        metadata_path = os.path.join(entry.path, 'metadata.json')
        if not os.path.exists(metadata_path):
            # generate the metadata.json file with values from the folder
            metadata['name'] = entry.name
            sizes, styles = get_icon_details(entry.path)
            metadata['size'] = sizes
            metadata['style'] = styles
            metadata['keyword'] = 'fluent-icon'
            metadata['description'] = ''
            metadata['metaphor'] = []
            metadata['comment'] = 'This was missing from the original repo so I added it in. Description and metaphor fields should get filled out if possible!'
            with open(metadata_path, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2)