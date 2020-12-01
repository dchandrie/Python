current_temp = float(input("what is the current temp? "))
wind_speed = float(input("What is the current wind speed? "))
if current_temp>50 or wind_speed<3:
    print("Wind Chill is in Deg. F. " + str(current_temp))
else:
    wind_chill = 34.75 +0.6215*current_temp - 34.75*wind_speed**0.16 + 0.4275*current_temp*wind_speed**0.16
    print("Wind_chill is Deg. F. "+ str(wind_chill))