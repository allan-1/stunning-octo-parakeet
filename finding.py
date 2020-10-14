import fnmatch
import os

root_dir = "/home/allan/code/"
pattern = ".py"

for root, dirs, files in os.walk(root_dir):
    for filename in fnmatch.filter(files, pattern):
        print(os.path.join(root, filename))
