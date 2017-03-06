from PIL import Image


class ScaleZip:
    """
    Scale images if directory.
    """
    def process_files(self, temp_directory, n, m):
        """
        Scale each image in the directory to n*m size
        :param temp_directory: directory path
        :param n: horizontal size
        :param m: vertical sie
        :return: None
        """
        for filename in temp_directory.iterdir():
            im = Image.open(str(filename))
            scaled = im.resize((n, m))
            scaled.save(str(filename))
