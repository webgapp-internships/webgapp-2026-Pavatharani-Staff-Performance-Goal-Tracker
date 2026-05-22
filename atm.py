class atm():
    def __init__(self,pin):
        self.__pin = pin
    def check_pin(self,entered_pin):
        if self.__pin == entered_pin:
            print("correct PIN")
        else:
            print("wrong PIN")
atm = atm(2327)
user_pin = int(input("Enter your PIN :"))
atm.check_pin(user_pin)
