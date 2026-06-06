# logical operators = evaluate multiple conditions (or, and, not)
#                     or = at least one condition must be True
#                     and = all conditions must be True
#                     not = invert the condition (not false, not true)

temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining: 
    print("The outdoor event is cancelled!")
else:
    print("The outdoor event is still scheduled.")

temp = 20
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT outside!")
    print("It is SUNNY")
elif temp <= 0 and is_sunny:
    print("It is COLD outside!")
    print("It is SUNNY")
elif temp < 28 and temp > 0 and is_sunny:
    print("It is warm outside!")
    print("It is SUNNY")
elif temp >= 28 and not is_sunny:
    print("It is HOT outside!")
    print("It is CLOUDY")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside!")
    print("It is CLOUDY")
elif temp < 28 and temp > 0 and not is_sunny:
    print("It is warm outside!")
    print("It is CLOUDY")