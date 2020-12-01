number = input("Give me a number")
number1 =(int(number))
def Absolute_Value():
    if number <0 :
        AbsoluteValue = 0 - number1
    else:
        AbsoluteValue = number1
    return AbsoluteValue
print(str(Absolute_Value()))