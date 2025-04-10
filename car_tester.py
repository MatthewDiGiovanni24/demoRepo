from car import Car

lst = []
with open("cars.txt") as file:
    for line in file:
        x = line.split()
        lst.append(Car(x[0], x[1], int(x[2]), int(x[3])))

for c in lst:
    print(c)
    c.drive()
    print(c.get_gas_tank())
    print(c.get_odometer())
    print()
