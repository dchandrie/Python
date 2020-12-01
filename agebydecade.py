age = float(input("What is your age?  "))
if age >= 50 and age <= 60:
    print("You are a Quinquagenarian", age)
elif age >=40 and age <= 50:
    print("You are a Quadragenarian")
elif age >= 30 and age <= 40: 
    print ("You are a Tricenarian")
elif age >= 20 and age <= 30:
    print ("You are a Vicenarian")
elif age >= 10 and age <=20:
    print ("You are a Denarian")
elif age > 60:
    print("You are too young or too old dear!!!!")