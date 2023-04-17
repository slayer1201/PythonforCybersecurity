#example 1
temp = 5
if temp < 10 and temp > 0:
    if temp > 5:
        print("Level 1")
    elif temp < 5:
        print("Level 2")
    else:
        print("Level 3")
elif temp == 5:
    print("Level 4")
else:
    print("Level 5")

#Good Day
good_day = input("Is today a good day? (y/n ")
if good_day == "y" or good_day == "yes":
    print("Yes it is")
else:
    print("I guess its not")

# Not Possable
temp = int(input("What is the temperature? "))
if temp < 10 and temp > 0:
    if temp > 5:
        print("Level 1")
    elif temp < 5:
        print("Level 2")
    else:
        print("Level 3")
#NOT Possable\/
elif temp == 5:
    print("Level 4")
else:
    print("Level 5")