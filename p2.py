class Department:

    def __init__(self, student_name):
        self.student_name = student_name

    def details(self):
        return "Student Details"


# Child class
class CSE(Department):

    def details(self):
        return f"{self.student_name}: CSE Department"


# Another child class
class IT(Department):

    def details(self):
        return f"{self.student_name}: IT Department"


# Student inherits CSE
class Student(CSE):

    def __init__(self, student_name, project):

        # Call parent constructor
        super().__init__(student_name)

        self.project = project

    def show_project(self):
        return f"{self.student_name} is doing {self.project} project"


# Objects
s1 = CSE("Arun")

s2 = IT("Kumar")
s3 = Student("Santhosh", "Management System")


# Output
print(s1.details())

print(s2.details())

print(s3.details())

print(s3.show_project())