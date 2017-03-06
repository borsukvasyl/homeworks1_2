class ZipReplace:
    """
    Replace words in directory
    """
    def __init__(self, search_string, replace_string):
        """
        Construct replaced words.
        :param search_string: word to replace
        :param replace_string: new word
        """
        self.search_string = search_string
        self.replace_string = replace_string

    def process_files(self, temp_directory):
        """
        Replace all searched words in directory to
        a new word
        :param temp_directory: directory path
        :return: None
        """
        for filename in temp_directory.iterdir():
            with filename.open() as file:
                contents = file.read()
            contents = contents.replace(
                    self.search_string, self.replace_string)
            with filename.open("w") as file:
                file.write(contents)
