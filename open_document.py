import os

def open_file(file_path):
    if os.path.exists(file_path):
        os.startfile(file_path)
    else:
        print("❌ File not found:", file_path)