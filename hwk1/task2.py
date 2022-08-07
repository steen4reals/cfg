"""

TASK 2

Write a base class to represent a student. Below is a starter code.
Feel free to add any more new features to your class.
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student.

"""


class Student:

    def __init__(self, name, age, id, stream):
        self.name = name
        self.age = age
        self.id = id
        self.stream = stream
        self.subjects = dict()


class CFGStudent(Student):
    def __int__(self):
        Student.__init__(self)

# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subjects (add/remove new subject and its grade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)

    def add_subject(self, subject_and_grade):
        self.subjects.update(subject_and_grade)

    def remove_subject(self, subject):
        self.subjects.pop(subject)

    def show_subjects(self):
        for subject, grade in self.subjects.items():
            print(f"{subject} ... {grade}")

    def get_mark(self):
        total = 0
        for value in self.subjects.values():
            total += value
        return total/len(self.subjects)


student = CFGStudent('Christina', 20, 123, 'Software')

student.add_subject({'Python': 90})
student.add_subject({'SQL': 100})
student.add_subject({'OOP': 95})

student.show_subjects()
print(student.get_mark())
