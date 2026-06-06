# collection = single "variable" used to store multiple values
#   List     = [] ordered and changeable, Duplicates OK
#   Tuple    = () ordered and unchangeable, Duplicates OK, FASTER
#   Set      = {} unordered and immutable, but Add/Remove OK, NO duplicates

fruits = ["apple", "orange", "banana", "coconut"]
#print(dir(fruits))
#print(help(fruits))
#print(fruits[0])
#print(len(fruits))
#print("apple" in fruits)

#fruits[0] = "pineapple"
#fruits.append("pineapple")
#fruits.remove("apple")
#fruits.insert(1, "pineapple")
#fruits.sort()
#fruits.reverse()
#fruits.clear()
#print(fruits.index("coconut"))
#print(fruits.count("banana"))

for fruit in fruits:
    print(fruit)