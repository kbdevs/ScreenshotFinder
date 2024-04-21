import os
import shutil
from tqdm import tqdm

def search_directory(directory):
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            if dir == "screenshots":
                if not os.path.exists("Exported Screenshots"):
                    os.makedirs("Exported Screenshots")
                files = os.listdir(os.path.join(root, dir))
                progress_bar = tqdm(files, desc="Copying screenshots from found folder: ", unit="file")
                for file_name in progress_bar:
                    source_file = os.path.join(os.path.join(root, dir), file_name)
                    dest_file = os.path.join("Exported Screenshots", file_name)
                    shutil.copy2(source_file, dest_file)  # copy2 preserves metadata
                    progress_bar.set_postfix(file=file_name)
                    progress_bar.update(1)

# Example usage
directory = input("Enter the directory to search: ")
search_directory(directory)
print("All found screenshots have been copied to the 'Exported Screenshots' folder. :)")
