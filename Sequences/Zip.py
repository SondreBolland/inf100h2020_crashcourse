names = ["Sondre", "Kari", "Bob", "Johanna"]
student_numbers = [4, 1, 3, 2]
grades = ["C", "A", "D", "B"]

zipped_elements = zip(names, student_numbers, grades)
print(list(zipped_elements))

name_to_grade = dict(zip(names, grades))
print(name_to_grade)
print(name_to_grade['Sondre'])