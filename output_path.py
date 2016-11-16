
import glob
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--out_path')
args = parser.parse_args()

#files = glob.glob(args+'.*')

files = glob.glob('/hogehoge/*.png')

for file in files:
    print(file)

