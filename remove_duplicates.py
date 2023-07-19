import os
import sys
import hashlib

def compute_hash(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def remove_duplicates(directory):
    duplicates = {}
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_hash = compute_hash(file_path)
            if file_hash in duplicates:
                print(f"Removing duplicate: {file_path}")
                os.remove(file_path)
            else:
                duplicates[file_hash] = file_path

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python remove_duplicates.py <directory_path>")
        sys.exit(1)

    target_directory = sys.argv[1]
    print(f"Searching for duplicates in: {target_directory}")
    remove_duplicates(target_directory)
    print("Duplicate removal process completed.")
