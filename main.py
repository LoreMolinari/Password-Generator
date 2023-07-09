import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
special = "*?.,;:[]\{\}()"

mix = lower + upper + number + special

length = int(input("Lunghezza della password? \t"))

password = "".join(random.sample(mix, length))

print("Password suggerita:", password)
