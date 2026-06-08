import random
import string

chars = (
    random.choices(string.ascii_uppercase, k=2) +
    random.choices(string.ascii_lowercase, k=2) +
    random.choices(string.digits, k=2) +
    random.choices(string.punctuation, k=2)
)

random.shuffle(chars)

password = "".join(chars)

print("Your generated password is:", password)