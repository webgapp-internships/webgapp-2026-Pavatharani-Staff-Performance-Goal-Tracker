class pin():
    def __init__(self,pin):
        self.__pin = pin
    def getpin(self):
        return self.__pin
    def setpin(self,pin):
        self.__pin = pin
s1 = pin(2327)
print(s1.getpin())
s1.setpin(2706)
print(s1.getpin())
