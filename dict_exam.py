# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
student_list = { 'name': 'Özge', 'school': 'Rahm Kula Anadolu Lisesi', 'grades': (66,77,88)}
student_mapping = {name[1]: name for name in student_list}

def average_grade(data): #data:argument
    grades = data['grades']  #data dictionary
    return sum(grades) / len(grades)

def average_grade_all_students(student_list):
    total = 0
    count = 0
    for name in student_list:
        name,school, grade = student_mapping[name]
        total += sum(student_list['grades'])
        count += len(student_list['grades'])
    return total / count