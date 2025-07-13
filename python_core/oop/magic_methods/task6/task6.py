import os

class Cd:
    def __init__(self, path):
        if not os.path.isdir(path):
            raise ValueError(f"Directory '{path}' does not exist or is not a directory.")
        self.new_dir = path

    def __enter__(self):
        self.old_dir = os.getcwd()
        os.chdir(self.new_dir)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.old_dir)

