import json
import os


cwd = os.getcwd()
assets_dir = os.path.join(cwd, 'assets')


def get_icon_styles(icon_dir):
    styles = []
    svg_dir = os.path.join(icon_dir, 'SVG')
    for entry in os.scandir(svg_dir):
        if entry.is_file() and entry.name.endswith('.svg'):
            style = entry.name.split('_')[-1].split('.')[0]
            if style not in styles:
                styles.append(style)
    return styles


for entry in os.scandir(assets_dir):
    if not entry.is_dir():
        continue

    metadata_path = os.path.join(entry.path, 'metadata.json')
    if not os.path.exists(metadata_path):
        continue
    
    with open(metadata_path, 'r', encoding='utf-8') as f:
        metadata = json.load(f)

    metadata['style'] = get_icon_styles(entry.path)

    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2)