
import os

def is_mounted_directory(path: str) -> bool:
    """
    Check if a directory is a mounted directory.
    """
    return os.path.ismount(path)

def recursive_scan(path: str):
    """
    Recursively scan a directory for mkv files.
    """
    inputs = []

    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith('.mkv'):
                inputs.append(os.path.join(root, file))

    return inputs