class student:
    def __init__(self, name, marks):
        self. name = name
        self. marks = marks
    def result(self):
        if self.marks >= 50:
            return "pass"
        else:
            return "fail"
    def show(self):
        print(self. name,self. marks)
s1= student("pavi",79)
s2= student("harini",55)
s3=student("bency",83)
s1.show()
s2.show()
s3.show()
print("result",s1.result())
print("result",s2.result())
print("result",s3.result())