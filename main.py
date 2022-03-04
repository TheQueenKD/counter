"""
end result:
input number
count from 1 to that number

example:
input: 4
1
2
3
4

layout:
input from user
range
for loop
"""


count = int(input('Number please:\t') or 2)
if count <= 0:
    numbers = range(count, 1)
else:
    numbers = range(1, 1 + count)
for number in numbers:
    print(number)
