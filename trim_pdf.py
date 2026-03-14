import os
import shutil

assets_dir = os.path.join(os.getcwd(), 'assets')

for root, dirs, files in os.walk(assets_dir):
    if 'PDF' in dirs:
        pdf_path = os.path.join(root, 'PDF')
        shutil.rmtree(pdf_path)