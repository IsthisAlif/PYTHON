# FizzBuzz = print the numbers from 1 to 100, but 
#            for multiples of three, print "Fizz" instead, 
#            for multiples of five, print "Buzz", and 
#            for numbers that are multiples of both, print "FizzBuzz"

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)