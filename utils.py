import os

def get_test_files_in_folder(folder_path):
    test_files = []
    for filename in os.listdir(folder_path):
        if filename.startswith("test"):
            file_path = os.path.join(folder_path, filename)
            test_files.append(file_path)
    return test_files