#variables and annotations

text: str = "hello"
dec_num: float = 1.23
count: int = int(0)
toggle: bool = True
numbers: list[float] = [1, 2, 3]

#conditional statement

if dec_num < 1:
    print("number is less than 1")
elif dec_num < 2:
    print("number is less than 2")
else:
    print("number is equal or greater than 2")

#operators

# == Equal
# != not equal
# < less than
# > greater than
# <= less than or equal
# >= greater or equal
# in element is member of sequence
# not in element is not member of sequence
# and true if both true
# or true if one is true
# not reserved result
# is true if variables are same object (memory location)
# is not true if variables are not same object (memory location)

#loop structures

for current in range(5):
    print("current" + str(current))
    break

feed = "placeholder"
while feed !="":
    feed = input("insert text(empty stops):")
    print(feed)
    continue

#function

def multiply(multiplicant: float, multiplier: float) -> float:
    product = multiplicant * multiplier
    return product

original_price = 1000
vat_rate = 1.24
vat_price = multiply(original_price, vat_rate)
print("VAT Price: {} * {} = {}".format(original_price, vat_rate, vat_price))

#error handling

fraction: float | None = None
try:
    fraction = 2 / 0
except ZeroDivisionError:
    print("Can't divide with zero")
finally:
    print("Fraction: " + str(fraction))

#module import

from math import pi
import sys

print(pi)
sys.exit(0) 

#filehandle

filehandle = open ("filename.txt", 'r', encoding="utf-8")
rows = filehandle.readlines()
filehandle.close()
content = ''.join(rows)
print(content)