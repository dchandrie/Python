#calculation of %
inloop = True
num = int(input("Give me number: "))
while inloop:
    if num < 0:
        print("Invalid Entry!!!!")
        break
    percentage = 1000/num*100
    print("Percentage : "+str(percentage))
courses = ["Math", "Science", "Geography"]
