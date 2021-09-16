from os import listdir
from os.path import isfile, join
from typing import List


def list_folder(path: str) -> List[str]:
    files = [f for f in listdir(path) if isfile(join(path, f))]
    return files
