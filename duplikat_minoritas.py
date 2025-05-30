import os
import shutil
import random

def oversample_minority_classes(parent_dir, target_count=400):
    for class_name in os.listdir(parent_dir):
        class_dir = os.path.join(parent_dir, class_name)
        if not os.path.isdir(class_dir):
            continue
        files = [f for f in os.listdir(class_dir) if os.path.isfile(os.path.join(class_dir, f))]
        n_files = len(files)
        if n_files >= target_count:
            continue  # Sudah cukup
        print(f"Oversampling {class_name}: {n_files} -> {target_count}")
        while len(files) < target_count:
            file_to_copy = random.choice(files)
            src = os.path.join(class_dir, file_to_copy)
            # Buat nama file baru agar tidak overwrite
            new_name = f"dup_{len(files)}_{file_to_copy}"
            dst = os.path.join(class_dir, new_name)
            shutil.copy(src, dst)
            files.append(new_name)

# Jalankan untuk train, valid, dan test
oversample_minority_classes('converted/train', target_count=400)
oversample_minority_classes('converted/valid', target_count=100)
oversample_minority_classes('converted/test', target_count=50)