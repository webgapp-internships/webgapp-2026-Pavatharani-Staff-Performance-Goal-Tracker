name = "Tharani"
print("NAME:",name)

password=" "
while  password != "DOB":
     password = input("Enter you password : ")
print("Login successfully")

sub= ["Tamil","English","Maths","Science","Social"]
total = 0
for sub in sub:
    marks1 = int(input("ENTER YOUR " + sub + " MARK : " ))
    total =total + marks1  
    if marks1 >= 90:
        print("O GRADE")
    elif marks1 >= 75:
        print("A GRADE")
    elif marks1 >= 55:
       print("B GRADE")
    elif marks1 >= 35:
       print("C GRADE")
    else:
       print("SORRY : FAILED")

print("----TOTAL----")
print ("Total" ,total)
if total >=150:
    print("PASS")
else:
    print("FAILED")