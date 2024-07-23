
import os
import random
import shutil
import yaml

# Kaynak ve hedef dizinler
source_dir = r"PATH_TO_YOUR_SOURCE_DIRECTORY"  # kaynak dizin
target_dir = r"PATH_TO_YOUR_TARGET_DIRECTORY"  # hedef dizin

# Etiket klasörlerinin listesi
labels = [
    "belirsiz", "sifir", "on", "yirmi", "otuz", "kirk", "elli", 
    "altmis", "yetmis", "seksen", "doksan", "yuz"
]

# Klasörleri oluştur
os.makedirs(os.path.join(target_dir, "train"), exist_ok=True)
os.makedirs(os.path.join(target_dir, "test"), exist_ok=True)

# Veriyi karıştır ve dağıt
for label in labels:
    label_source_dir = os.path.join(source_dir, "train", label)
    label_target_train_dir = os.path.join(target_dir, "train", label)
    label_target_test_dir = os.path.join(target_dir, "test", label)
    
    os.makedirs(label_target_train_dir, exist_ok=True)
    os.makedirs(label_target_test_dir, exist_ok=True)
    
    # Dosya kontrolü
    if not os.path.exists(label_source_dir):
        print(f"Warning: Source directory '{label_source_dir}' does not exist.")
        continue

    image_files = [f for f in os.listdir(label_source_dir) if f.lower().endswith(".jpg") or f.lower().endswith(".png")]
    random.seed(42)  # Karıştırma işlemini tekrarlanabilir hale getirir
    random.shuffle(image_files)
    
    train_count = int(len(image_files) * 0.80)
    
    for i, image_file in enumerate(image_files):
        source_image_path = os.path.join(label_source_dir, image_file)
        if i < train_count:
            target_image_path = os.path.join(label_target_train_dir, image_file)
        else:
            target_image_path = os.path.join(label_target_test_dir, image_file)
        
        shutil.copy(source_image_path, target_image_path)

print("Data set created!")

# YAML dosyasını oluştur
data_yaml = {
    "train": "../train",
    "test": "../test",
    "nc": len(labels),
    "names": labels
}

with open(os.path.join(target_dir, "dataset.yaml"), "w") as yaml_file:
    yaml.dump(data_yaml, yaml_file)

print("YAML file created!")
