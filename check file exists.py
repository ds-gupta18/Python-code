# 1. os.path.exists

import os

file_name = "practice.txt"

if os.path.exists(file_name):
    print("file exists")
else:
    print("file does not exist")


file_name2 = "C:/Users/dsgup/PyCharmMiscProject/practice2.txt"

if os.path.exists(file_name2):
    print("file exists")
else:
    print("file does not exist")


# 2. pathlib.path.exists()

from pathlib import Path

file_name = Path("C:/Users/dsgup/PyCharmMiscProject/practice2.txt")
file_name = Path("C:/Users/dsgup/PyCharmMiscProject/practice11.txt")

if file_name.exists():
    print("file exists. Can't create!")
else:
    print("file does not exist, creating it")
    fh = open(file_name, "xt")
    fh.write("Some content")
    fh.close()