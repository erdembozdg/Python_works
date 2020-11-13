import os
import sys
import shutil
import zipfile
from pathlib import Path

class ZipProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.temp_directory = Path('unzipped{}'.format(filename[:-4]))

    def process_zip(self):
        self.unzip_files()
        self.process_files()
        self.zip_files()

    def unzip_files(self)
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.filename) as zip:
            zip.extractall(str(self.temp_directory))

    def zip_files(self):
        with zipfile.ZipFile(self.filename, 'w') as file:
            for fname in self.temp_directory.iterdir():
                file.write(str(fname), fname.name)
        shutil.rmtree(str(self.temp_directory))

class ZipReplace(ZipProcessor):
    def __init__(self, filename, search_str, replace_str):
        super().__init__(filename)
        self.search_str = search_str
        self.replace_str = replace_str

    def process_files(self):
        for fname in self.temp_directory.iterdir():
            with fname.open() as f:
                contents = f.read()
            contents = contents.replace(self.search_str, self.replace_str)
            with fname.open('w') as f:
                f.write(contents)

if __name__ == '__main__':
    ZipReplace(*sys.argv[1:4]).process_zip()