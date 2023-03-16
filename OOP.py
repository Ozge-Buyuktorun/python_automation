class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
     
    def average_grade(self):
          return sum(self.grades)/len(self.grades) 
     
student = Student("Bob",(100,54,27,95,47))
student2 = Student("Jenny",(87,34,57,55,97))

print(student.name)
print(f"All note's average is : {student.average_grade()}")
print(f"{student.name} person's all grade is : {student.grades}")

print(student2.name)
print(f"All note's average is : {student2.average_grade()}")
print(f"{student2.name} person's all grade is : {student2.grades}")


