
print("=== get abspath ===")

## stable
from pathlib import Path
print(Path(__file__).resolve().parent.joinpath('tmp'))


## error if used in Windows
from os.path import abspath,dirname,join
print(''.join([dirname(abspath(__file__)), '/', 'tmp']))


print("=== get filename ===")
test_path = "/Users/thatano/works/tmp.csv"

## name_with_suffix (basename)
print(Path(test_path).name)
## name_without_suffix
print(Path(test_path).stem)
## suffix
print(Path(test_path).suffix)
## parent directory
print(Path(test_path).parent)


print("=== file I/O ===")
import os

with open('test.txt', mode = 'wt') as f:
	f.write("テスト\nテスト")


with open('test.txt', mode = 'rt') as f:
	for line in f.readlines():
		print(line.strip())

print("=== make/remove file ===")

import shutil

shutil.copy2("test.txt", "test_copy.txt")

ls_file_name = os.listdir()

print("=== file list ===")
for file in ls_file_name:
	print(file)

shutil.move("test_copy.txt", 'backup/.')
shutil.move("backup/test_copy.txt", "backup/test_bkup.txt")

os.remove("test.txt")

