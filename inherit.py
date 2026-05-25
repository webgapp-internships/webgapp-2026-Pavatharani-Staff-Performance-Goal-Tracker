class project:

    def __init__(self, student_name):
        self.student_name = student_name

    def details(self):
        return "Project details"


class project_name1(project):

    def details(self):
        return f"{self.student_name}: front end development"


class project_name2(project):

    def details(self):
        return f"{self.student_name}: backend development"


class project_name3(project):
    def details(self):
         return f"{self.student_name}: Full stack development "


s1 = project_name1("sugasan")
s2 = project_name2("pavi")
s3 = project_name3("harini")


print(s1.details())

print(s2.details())

print(s3.details())