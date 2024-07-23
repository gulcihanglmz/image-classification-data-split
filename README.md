# Image Dataset Splitter

📂 A tool for splitting image datasets into training and testing sets for classification tasks. Useful for preparing data for machine learning models.

## Features

- Splits image datasets into training and testing subsets.
- Supports organizing images by classification labels.
- Generates a YAML configuration file for dataset management.

## Installation

1. **Clone the repository:**
   ```
   git clone https://github.com/Gulciha-n/image-classification-data-split.git
   cd image-classification-data-split
   ```

3. **Install required packages:**

   ```bash
   pip install pyyaml
   ```

## Usage

1. **Prepare your dataset:**

   Ensure your source directory is structured as follows:

   ```
   source/
   └── train/
       ├── belirsiz/
       ├── sifir/
       ├── on/
       ├── yirmi/
       ├── otuz/
       ├── kirk/
       ├── elli/
       ├── altmis/
       ├── yetmis/
       ├── seksen/
       ├── doksan/
       └── yuz/
   ```

   Here, `source` is your dataset directory, and each subdirectory (e.g., `belirsiz`, `sifir`, etc.) contains images corresponding to the classification labels.

2. **Update the script with your paths:**

   Edit the `main.py` file and update the `source_dir` and `target_dir` variables with your directory paths.

   ```python
   source_dir = r"PATH_TO_YOUR_SOURCE_DIRECTORY"  # source directory
   target_dir = r"PATH_TO_YOUR_TARGET_DIRECTORY"  # target directory
   ```

3. **Run the script:**

   Execute the following command to run the script:

   ```bash
   python main.py
   ```

   This will organize and split your image dataset into training and testing sets, and generate a `dataset.yaml` file in the target directory.

   After running the script, your target directory structure will be:

   ```
   train_test_images/
   ├── train/
   │   ├── belirsiz/
   │   ├── sifir/
   │   ├── on/
   │   ├── yirmi/
   │   ├── otuz/
   │   ├── kirk/
   │   ├── elli/
   │   ├── altmis/
   │   ├── yetmis/
   │   ├── seksen/
   │   ├── doksan/
   │   └── yuz/
   └── test/
       ├── belirsiz/
       ├── sifir/
       ├── on/
       ├── yirmi/
       ├── otuz/
       ├── kirk/
       ├── elli/
       ├── altmis/
       ├── yetmis/
       ├── seksen/
       ├── doksan/
       └── yuz/
   ```

   A `dataset.yaml` file will also be created in the `train_test_images` directory.

## Configuration

- **source_dir:** Directory where your image data is located.
- **target_dir:** Directory where the split data will be saved.
- **labels:** List of classification labels used for organizing images.

## License

This project is licensed under the MIT License 

