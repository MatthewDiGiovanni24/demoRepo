name = input("Enter your name: ")
print("Hello", name)

try:
    num = int(input("Enter a number: "))
    print("you entered", num)
    add = num + 2
    print("2 more is ", add)
except:
    print("number was not entered")

with open("movies.txt") as file:
    for line in file:
        print(line.strip())

with open("heights.txt") as file:
    for line in file:
        info = line.strip().split()
        info[2] = int(info[2])
        print(info)

name = input("Enter name of text file: ")
with open(name) as file:
    for i, line in enumerate(file):
        print(str(i + 1) + ". " + line.strip())
