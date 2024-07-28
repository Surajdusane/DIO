import shutil
import os

def zip_folder(folder_path, zip_path):
    """
    Compresses a folder into a zip file.

    :param folder_path: The path to the folder to be compressed.
    :param zip_path: The path where the zip file should be saved.
    """
    # Ensure the folder path is valid
    if not os.path.isdir(folder_path):
        raise ValueError(f"The folder path '{folder_path}' is not a valid directory.")
    
    # Create the zip file
    shutil.make_archive(base_name=zip_path, format='zip', root_dir=folder_path)

    print(f"Folder '{folder_path}' has been compressed into '{zip_path}.zip'.")
