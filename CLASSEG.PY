class student:
    def detail(self,name,marks):
        if marks >=50:
             result="pass"
        else:
             result="fail"
        return name,marks,result
s= student()
print("-------STUDENT MARK DETAILS--------")
print(s.detail("Harini",67))
print(s.detail("Pavi",74))
print(s.detail("Sugasan",90))
print("-----------END----------")