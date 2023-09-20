import os
import shutil

def to_working(extension=".tar.gz"):
    source_folder = os.getcwd()  # Get the current incoming directory path
    destination_folder = source_folder.replace("incoming", "working")
    # Check if the destination folder exists, and create it if not
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterate over files in the source folder (incoming directory)
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)
        if filename.endswith(extension):
            # Check if the file is a .tar.gz file
            destination_path = os.path.join(destination_folder, filename)
            shutil.copyfile(source_path, destination_path)
            print(f"Copied {filename} to {destination_folder}")

# Example usage: Copy all .tar.gz (by default) files from current incoming directory to the working directory.
# Takes an extension eg .txt as an optional argument
if __name__ == '__main__':
  to_working()
  to_working(".txt")
