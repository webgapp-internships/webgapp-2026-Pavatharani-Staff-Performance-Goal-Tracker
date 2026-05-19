name = "Tharani"
print("NAME:",name)

password=" "
while  password != "DOB":
     password = input("enter you password : ")
print("Login successfully")

sub= ["TAMIL","ENGLISH","MATHS","SCIENCE","SOCIAL"]
total = 0
for sub in sub:
    marks1 = int(input("ENTER YOUR " + sub + " MARK : " ))
    total =total + marks1  
    if marks1 >= 90:
        print("DISTINCTION")
    elif marks1 >= 75:
        print("FIRST CLASS")
    elif marks1 >= 55:
       print("SECOND CLASS")
    elif marks1 >= 35:
       print("THIRD CLASS")
    else:
       print("SORRY : FAILED")

print("----TOTAL----")
print ("Total" ,total)
if total >=150:
    print("PASS")
else:
    print("FAILED")