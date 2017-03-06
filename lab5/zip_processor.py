import shutil
import zipfile
from pathlib import Path


class ZipProcessor:
    """
    Unzip file -> process -> zip file.
    """
    def __init__(self, process, zipname):
        """
        Construct process and path to filename.
        :param process: process object
        :param zipname: zip file name
        """
        self.process = process
        self.zipname = zipname
        self.temp_directory = Path("unzipped-{}".format(
                zipname[:-4]))

    def process_zip(self, *args):
        """
        Unzip file -> process -> zip file.
        :param args: args for process
        :return: None
        """
        self.unzip_files()
        self.process.process_files(self.temp_directory, *args)
        self.zip_files()

    def unzip_files(self):
        """
        Unzip file.
        :return: None
        """
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.zipname) as zip:
            zip.extractall(str(self.temp_directory))

    def zip_files(self):
        """
        Zip file
        :return: None
        """
        with zipfile.ZipFile(self.zipname, 'w') as file:
            for filename in self.temp_directory.iterdir():
                file.write(str(filename), filename.name)
        shutil.rmtree(str(self.temp_directory))

'''import scale_zip
zip_processor = ZipProcessor(scale_zip.ScaleZip(), "test_im.zip")
zip_processor.process_zip(2000, 1000)'''
