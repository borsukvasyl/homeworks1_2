import read_field, ship_info, generate_field, field_to_str


print("checking correct input")
field = read_field.read_field("field1.txt")
field_to_str.field_to_str(field)
print("Field is correct: " + str(read_field.is_valid(field))) # field1.txt is correct
print(45 * "-")
print("checking incorrect input")
field = read_field.read_field("field2.txt")
field_to_str.field_to_str(field)
print("Field is correct: " + str(read_field.is_valid(field))) # field2.txt is incorrect
print(45 * "-")

print("Checking field generator")
correct = 0
incorrect = 0
for i in range(1000):
    field = generate_field.generate_field()
    if read_field.is_valid(field):
        correct += 1
    else:
        incorrect += 0
print("generations: 1000" + "\ncorrect: " + str(correct) + "\nincorrect: " + str(incorrect))
