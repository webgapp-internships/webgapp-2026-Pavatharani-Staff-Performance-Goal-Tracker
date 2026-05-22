class shape:
    def area(self): return 0
class circle(shape):
    def __init__(self,r): self.r = r
    def area(self):
        return 3.14 * self.r**2
class rectangle(shape):
    def __init__(self,w,h): 
        self.w,self.h=w,h
    def area(self):
        return self.w * self.h
shapes =[circle(5),rectangle(4,6)]
for shape in shapes:
    print(shape.area())