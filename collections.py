# lists (array)
cart = ["apples", "bananas", "cherries"]
print(cart)

cart.append("donuts")
cart.append("eggs")
cart.append("flour")
print(cart)

if "cherries" in cart:
    cart.remove("cherries")
print(cart)

cart.pop(2)
print(cart)
cart.pop()
print(cart)
cart.reverse()
print(cart)
cart.sort()
print(cart)

cart.append("bananas")
cart.append("grapes")
cart.append("oranges")
print(cart)
fruitbasket = cart[3:]
print(fruitbasket)

squares = []
for i in range(1, 11):
    squares.append(i**2)
print(squares)

# list comprehension
squares = [x * x for x in range(1, 11)]
print(squares)

newcart = [x for x in cart if x.startswith("b")]
print(newcart)

lst = ["1", "2", "10"]
num_lst = [int(x) for x in lst]
print(num_lst)

Inventory = [0] * len(cart)
print(Inventory)
Inventory[0] = 1
print(Inventory)

# sets
empty = set()
num_sets = {1, 1, 3, 4}
print(num_sets)
lst = [1, 1, 1, 2, 2, 2, 3, 3, 4]
setlst = set(lst)
print(setlst)
lst = list(setlst)
print(lst)

st = {4, 10, 3, 7, 8}
print(st)
sorted(st)
print(st)


# dictionary
fav_snacks = {}
fav_snacks = {
    "kathleen": "tortilla chips",
    "ava": "chex mix",
    "emily": "buffalo chicken dip",
    "wade": "popcorn",
}
print(fav_snacks)
fav_snacks["lucas"] = "chocolate"
print(fav_snacks)

for key in fav_snacks:
    print(f"{key}'s favorite snack is {fav_snacks[key]}")
    # print(key + "'s" + "favorite snack is " + fav_snacks[key])

for key, value in fav_snacks.items():
    print(key, value)

if "Bob" in fav_snacks:
    print(fav_snacks["Bob"])
else:
    fav_snacks["Bob"] = "chips"

keys = fav_snacks.keys()
values = fav_snacks.values()
print(sorted(keys))
print(sorted(values))

fav_snacks["Alice"] = ["chips", "nuts"]
print(fav_snacks)
