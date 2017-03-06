class Document:
    """
    Represents common txt document.
    """
    def __init__(self):
        """
        Initialize document.
        """
        self.characters = []
        self.cursor = Cursor(self)

    def insert(self, character):
        """
        Insert character in the current cursor position.
        :param character: character
        :return: None
        """
        if len(character) > 1:
            raise IncorrectCharacter()
        if not hasattr(character, 'character'):
            character = Character(character)
        self.characters.insert(self.cursor.position,
                               character)
        self.cursor.forward()

    def delete(self):
        """
        Delete character in the current cursor position.
        :return: None
        """
        if self.cursor.position >= len(self.characters):
            raise NoSuchCharacter()
        del self.characters[self.cursor.position]

    def save(self, filename):
        """
        Save document in a filename.
        :param filename: filename
        :return: None
        """
        if not filename:
            raise IncorrectFilename
        f = open(filename, 'w')
        f.write(''.join(self.characters))
        f.close()

    @property
    def string(self):
        return "".join((str(c) for c in self.characters))


class Cursor:
    """
    Represents cursor in the file.
    """
    def __init__(self, document):
        """
        Initialize cursor.
        :param document: document object
        """
        self.document = document
        self.position = 0

    def forward(self):
        """
        Move cursor forward.
        :return: None
        """
        if self.position >= len(self.document.characters):
            raise CursorOutOfFileInTheEnd()
        self.position += 1

    def back(self):
        """
        Move cursor back.
        :return: None
        """
        if self.position - 1 < 0:
            raise CursorOutOfFileInTheBeginning()
        self.position -= 1

    def home(self):
        """
        Move cursor to the beginning of line.
        :return: None
        """
        while self.document.characters[
                    self.position - 1].character != '\n':
            self.position -= 1
            if self.position == 0:
                # Got to beginning of file before newline
                break

    def end(self):
        """
        Move cursor to the end of line.
        :return: None
        """
        while self.position < len(self.document.characters) and \
                        self.document.characters[
                            self.position].character != '\n':
            self.position += 1


class Character:
    """
    Represents character in the file.
    """
    def __init__(self, character,
                 bold=False, italic=False, underline=False):
        """
        Initialize character.
        :param character: character
        :param bold: bool
        :param italic: bool
        :param underline: bool
        """
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        """
        Return character string.
        :return: character string
        """
        bold = "*" if self.bold else ''
        italic = "/" if self.italic else ''
        underline = "_" if self.underline else ''
        return bold + italic + underline + self.character

class CursorOutOfFileInTheBeginning(Exception):
    pass

class CursorOutOfFileInTheEnd(Exception):
    pass

class NoSuchCharacter(Exception):
    pass

class IncorrectFilename(Exception):
    pass

class IncorrectCharacter(Exception):
    pass
