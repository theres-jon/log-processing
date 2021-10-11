import os
import sys
from typing import Generator 

class FileStream():
    
    @staticmethod
    def read_file(file_path: str):
        # Simple validation.
        # Future enhancement: Further file validation
        if os.path.isfile(file_path) is not True:
            sys.exit("Provided file does not exist: {file_path}")

        for line in open(file_path):
            yield line.strip()