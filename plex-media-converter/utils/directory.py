
import os

def is_mounted_directory(path: str) -> bool:
    """
    Check if a directory is a mounted directory.
    """
    return os.path.ismount(path)
