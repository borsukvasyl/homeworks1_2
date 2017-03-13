def all_prefixes(word):
    res = set()
    for char in range(len(word)):
        if word[char] == word[0]:
            for index in range(char + 1, len(word) + 1):
                # print(word[char:index])
                res.add(word[char:index])
    return res
