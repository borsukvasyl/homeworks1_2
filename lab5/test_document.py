import document


def test_insert(character):
    try:
        doc.insert(character)
        return True
    except document.IncorrectCharacter:
        return False


def test_delete():
    try:
        doc.delete()
        return True
    except document.NoSuchCharacter:
        return False


def test_forward():
    try:
        doc.cursor.forward()
        return True
    except document.CursorOutOfFileInTheEnd:
        return False


def test_back():
    try:
        doc.cursor.back()
        return True
    except document.CursorOutOfFileInTheBeginning:
        return False


def test_home():
    doc.cursor.home()


def test_end():
    doc.cursor.end()


def test_save(filename):
    try:
        doc.save(filename)
        return True
    except document.IncorrectFilename:
        return False


doc = document.Document()
doc.insert("1") # 1|
assert test_forward() == False, "Reached end of file"
assert test_back() == True, "Method back works wrong"
# |1
assert test_back() == False, "Reached beginning of file"
assert test_forward() == True, "Method forward works wrong"
# 1|
assert test_insert("12") == False, "Incorrect character"
test_insert("2")
# 12|
assert doc.string == "12" , "Method insert works wrong"
test_insert("\n")
# 12\n|
test_insert("3")
# 12\n3|
test_insert("4")
# 12\n34|
assert test_delete() == False, "Deleting wrong character"
test_back()
# 12\n3|4
assert test_delete() == True, "Method delete works wrong"
# 12\n3|
assert doc.string == "12\n3", "Method delete works wrong"
test_home()
# 12\n|3
test_insert("4")
# 12\n4|3
assert  doc.string == "12\n43", "Method home works wrong"
test_end()
# 12\n43|
test_insert("2")
# 12\n432|
assert  doc.string == "12\n432", "Method home works wrong"
assert  test_save("") == False, "Can`t save to unnamed file"
