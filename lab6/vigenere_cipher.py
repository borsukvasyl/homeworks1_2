class VigenereCipher:
    """
    Encode and decode text by keyword.
    """
    def __init__(self, keyword):
        self.keyword = keyword

    def extend_keyword(self, number):
        """
        Generates str of repeated keywords,
        which length is equal to number.
        :param number: length
        :return: str
        """
        repeats = number // len(self.keyword) + 1
        return (self.keyword * repeats)[:number]

    def encode(self, plaintext):
        """
        Encode text by keyword.
        :param plaintext: text
        :return: encoded text
        """
        plaintext = plaintext.replace(" ", "").upper()
        cipher = []
        keyword = self.extend_keyword(len(plaintext))
        for p, k in zip(plaintext, keyword):
            cipher.append(self.combine_character(p, k))
        return "".join(cipher)

    def decode(self, ciphertext):
        """
        Decode ciphered text by keyword.
        :param ciphertext: text
        :return: decoded text
        """
        plain = []
        keyword = self.extend_keyword(len(ciphertext))
        for p, k in zip(ciphertext, keyword):
            plain.append(self.separate_character(p, k))
        return "".join(plain)

    @staticmethod
    def combine_character(plain, keyword):
        """
        Combines character with keyword.
        :param plain: char
        :param keyword: keyword char
        :return: combined char
        """
        plain = plain.upper()
        keyword = keyword.upper()
        plain_num = ord(plain) - ord('A')
        keyword_num = ord(keyword) - ord('A')
        return chr(ord('A') + (plain_num + keyword_num) % 26)

    @staticmethod
    def separate_character(cypher, keyword):
        """
        Separate character from keyword.
        :param cypher: char
        :param keyword: keyword char
        :return: separated char
        """
        cypher = cypher.upper()
        keyword = keyword.upper()
        cypher_num = ord(cypher) - ord('A')
        keyword_num = ord(keyword) - ord('A')
        return chr(ord('A') + (cypher_num - keyword_num) % 26)
