import shutil
import os

from pathlib import Path
from argparse import ArgumentParser


# argument parser
parser = ArgumentParser()
parser.add_argument('-s', '--source', dest='source',
                    help='source dir name')
parser.add_argument('-d', '--destination', dest='destination',
                    help='destination dir name')
args = parser.parse_args()

# get child dirs of the source
dir_list = [os.path.join(args.source, filename)
            for filename in os.listdir(args.source)
            if os.path.isdir(os.path.join(args.source, filename))]

# create destination dir
Path(args.destination).mkdir(parents=True, exist_ok=True)

# move files to destination
for my_dir in dir_list:
    for root, dirnames, filenames in os.walk(my_dir):
        for filename in filenames:
            shutil.move(os.path.join(root, filename),
                        os.path.join(args.destination, filename))
            print(f'File {filename} was moved to {args.destination}')
