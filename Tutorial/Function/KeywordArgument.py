# Keyword Argument = an argument preceded by an identifier
#                    helps with readability
#                    order of arguments doesn't matter
#                    1. positional, 2. default, 3. KEYWORD, 4. arbitrary

# 1
def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello(greeting="Hello", title="Mr.", first="Spongbob", last="Squarepant")

# 2
for x in range(1, 11):
    print(x, end=" ")

# 3
print("1", "2", "3", "4", "5", sep="-")

# 4
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1,area=123,first=456,last=7890)
print(phone_num)