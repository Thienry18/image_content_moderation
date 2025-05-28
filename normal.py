import os
import shutil
from pathlib import Path

normal_images = list(Path("Normal").glob("*.png"))
total = len(normal_images)
train_end = int(0.7 * total)
valid_end = int(0.9 * total)

for i, img in enumerate(normal_images):
    if i < train_end:
        target = "converted/train/Normal"
    elif i < valid_end:
        target = "converted/valid/Normal"
    else:
        target = "converted/test/Normal"
    os.makedirs(target, exist_ok=True)
    shutil.copy(str(img), f"{target}/{img.name}")
