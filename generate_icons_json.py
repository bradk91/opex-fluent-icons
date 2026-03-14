import os
import json

cwd = os.getcwd()
asset_dir = os.path.join(cwd, 'assets')

all_icons = []
this_icon = {}
errors = []


def get_optimal_size(svg_dir):
    if not os.path.isdir(svg_dir):
        return None

    sizes = set()

    # Parse each filename to find all the sizes and throw in a set to dedupe them
    for icon_path in os.scandir(svg_dir):
        if icon_path.is_file() and icon_path.name.endswith('.svg'):
            size = icon_path.name.split('_')[-2]
            if size.isdigit():
                sizes.add(int(size))

    if not sizes:
        return None

    # Find the available size closest to 24px. Ties choose the smaller size.
    optimal_size = min(sizes, key=lambda s: (abs(s - 24), s))
    return str(optimal_size)

def get_icon_details(icon_path, metadata):
    icon_details = {}
    icon_details['name'] = '_'.join(icon_path.name.split('_')[2:-2])
    icon_details['style'] = icon_path.name.split('_')[-1].split('.svg')[0]
    icon_details['size'] = icon_path.name.split('_')[-2]
    icon_details['tags'] = metadata['metaphor']
    with open(icon_path, 'r', encoding='utf-8') as f:
        icon_details['svg'] = f.read()
    return icon_details

# Go through the assets directory and get all the icons to add to one flat file
for entry in os.scandir(asset_dir):
    if entry.is_dir():
        metadata_path = os.path.join(entry.path, 'metadata.json')
        if os.path.exists(metadata_path):
            with open(metadata_path, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
            svg_dir = os.path.join(entry.path, 'SVG')
            if os.path.exists(svg_dir):
                optimal_size = get_optimal_size(svg_dir)
                if optimal_size is None:
                    errors.append(f'No valid sizes found for {entry.name}')
                    continue
                for icon in os.scandir(svg_dir):
                    if icon.name.endswith('.svg') and (f'_{optimal_size}_' in icon.name):
                        this_icon = get_icon_details(icon, metadata)
                        all_icons.append(this_icon)                      

with open(os.path.join(cwd, 'icons2.json'), 'w', encoding='utf-8') as f:
    json.dump(all_icons, f, indent=2)

print(f'Generated icons2.json with {len(all_icons)} icons.')
if errors:
    print("Errors encountered:")
    for error in errors:
        print(f" - {error}")
else:
    print("No errors encountered.")