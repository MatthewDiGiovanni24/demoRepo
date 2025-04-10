print("Hello World!")

# this is a comment

"""
this is a 
longer comment
"""

# variables
x = 10
x = "hello"
x = [1, 2, 3]
print(x)

# math
x = 100
y = 10
result = x / y
# result is a float
print(int(result))

# floor division
x = 105
print(x // y)

min_val = min(1, 10, 50)
print(min_val)

raised = pow(2, 3)
print(raised)

raised = 2**3
print(raised)

# if statements
x = 0
if x > 0:
    print(" x is positive")
    x = 10
elif x < 0:
    print("X is negative")
else:
    print("x is 0")
    x = 12

start = 10
end = 100
if x >= start and x <= end:
    print("in range")
if x < start or x > end:
    print("in range")

# loops

counter = 0
while counter < 5:
    print(counter)
    counter += 1

for i in range(5):
    print(i, end=" ")
print()

lst = [2, 4, 6, 8]

for i in range(len(lst)):
    print(lst[i], end=" ")
print()

for val in lst:
    print(val)

for i, val in enumerate(lst):
    print(i, val, end=" ")
print()

# exercises

for i in range(1, 21):
    if i % 3 == 0:
        print(i, end=" ")
print()

counter = 1
sum = 0
while counter <= 50:
    if counter % 2 == 0:
        sum += counter
    counter += 1
print(sum)

numbers = [5, 8, 2, 15, 10, 3, 7]
for i in numbers:
    if i > 5:
        print(i, end=" ")
print()

lst = [1, 2, 3, 4, 5]
lst2 = []
sum = 0
for i in lst:
    sum += i
    lst2.append(sum)
for val in lst2:
    print(val, end=" ")
print()

# functions


def hello_world():
    print("hello world")


hello_world()


def hello(name):
    print("Hello", name)


hello("Matt")


def hello2(name="Bob"):
    print("Hello " + name)


hello2()

# exercise

lst = [0, 3, 8, 4, 5]
lst2 = [54, 23, 867, 2, 346]


def swap(lst):
    i = lst[0]
    lst[0] = lst[len(lst) - 1]
    lst[len(lst) - 1] = i


swap(lst)
print(lst)
swap(lst2)
print(lst2)

# strings

hello = "hello"
for c in hello:
    print(c, end=" ")
print()

print("hi" * 7)

# == compares values not memory address in python

if "hi" in "hi everyone":
    print("hi is there")

course = "Platform Computing"
plat = course[0:8]
comp = course[9:]
print(plat)
print(comp)
