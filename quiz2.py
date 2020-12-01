def temp (day):
    temperature = input()
    return temperature
sunday = temp("sunday")
monday = temp("monday")
tuesday=temp("tuesday")
wednesday=temp("wednesday")
thursday = temp("thursday")
friday = temp("friday")
saturday = temp("saturday")
sum = sunday+monday+tuesday+wednesday+thursday+friday+saturday
average_temp = float(sum)/7.0
print("The average weekly temperature is " +str(average_temp))