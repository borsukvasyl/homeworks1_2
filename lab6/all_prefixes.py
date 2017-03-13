def all_prefixes(word):
    """
    Find all prefixes in the word, which starts from first letter.
    :param word: word
    :return: set of prefixes
    """
    res = set()
    for char in range(len(word)):
        if word[char] == word[0]:
            for index in range(char + 1, len(word) + 1):
                res.add(word[char:index])
    return res
