class atm():
    def __init__(self,pin):
        self.__pin = pin
    def check_pin(self,entered_pin):
        if self.__pin == entered_pin:
            print("correct PIN")
        else:
            print("wrong PIN")
    def change_pin(self,old_pin,new_pin):
        if self.__pin == old_pin:
            self.__pin == new_pin
            print("PIN changed successfully")
        else:
            print("Incorrect PIN")
atm = atm(2327)
user_pin = int(input("Enter your PIN :"))
atm.check_pin(user_pin)
old_pin = int(input("Enter old PIN :"))
new_pin = int(input("Enter new PIN :"))
atm.change_pin(old_pin,new_pin)