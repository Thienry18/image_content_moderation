import os
import random
import shutil

def undersample_folder(folder_path, max_samples=400):
    nudity_dir = os.path.join(folder_path, "nudity")
    if not os.path.exists(nudity_dir):
        print(f"Folder {nudity_dir} tidak ditemukan.")
        return
    files = [f for f in os.listdir(nudity_dir) if os.path.isfile(os.path.join(nudity_dir, f))]
    if len(files) <= max_samples:
        print(f"Jumlah file nudity di {folder_path} sudah <= {max_samples}")
        return
    # Acak dan pilih file yang akan DIHAPUS
    files_to_remove = random.sample(files, len(files) - max_samples)
    for f in files_to_remove:
        os.remove(os.path.join(nudity_dir, f))
    print(f"Berhasil mengurangi file nudity di {folder_path} menjadi {max_samples}")

# Jalankan untuk train, valid, dan test
undersample_folder('converted/train', max_samples=400)
undersample_folder('converted/valid', max_samples=100)
undersample_folder('converted/test', max_samples=50)