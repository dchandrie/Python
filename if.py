is_male= input("Are you a male (True or False)")
is_tall= input("Are you tall (True or False")
if is_male and is_tall:
    print("you are a tall male")
elif is_male and not (is_tall):
    print("you are a male but not tall")
elif not(is_male)and is_tall:
    print("you are tall but not a male")
else:
    print("you are a not a male")