# Reverse a string
reverse = input("Enter a word: ")

reverse = reverse[::-1]
print(reverse)

# Check if a string is a palindrome
is_palindrome = input("Enter a word: ")

if is_palindrome == is_palindrome[::-1]:
    print(f"{is_palindrome} is a palindrome")
else:
    print(f"{is_palindrome} is not a palindrome")

# Find the first non-repeating character
is_non_repeating = input("Enter a word: ")

dict = {}

for char in is_non_repeating:
    dict[char] = dict.get(char, 0)+1

result = -1
for char in is_non_repeating:
    if dict[char] == 1:
        result = char
        break

print(f"This first non repeating character is '{result}'")

# Count character frequencies
character_freq = input("Enter a word: ")
dict = {}

for char in character_freq:
    dict[char] = dict.get(char, 0)+1

print(dict)

# Check if two strings are anagrams
string1 = input("Enter the first word: ").lower().replace(" ", "")
string2 = input("Enter the second word: ").lower().replace(" ", "")

if sorted(string1) == sorted(string2):
    print("Anagram")
else:
    print("Not an anagram")