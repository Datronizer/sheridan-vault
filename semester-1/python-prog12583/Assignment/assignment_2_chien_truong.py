import math

names   = ["Cheetah", "Royal Bengal Tiger", "African Lion", "Cougar"]
speeds  = [97, 64, 41, 88]
weights = [244, 484, 492, 302]
powers  = []

# Question 0.
for i in range(len(speeds)):
    rawPower     = speeds[i] * weights[i]
    roundedPower = round(rawPower / 1000)
    
    powers.append(roundedPower)
    
print("List method:")
print("Cat                 Speed   Weight  Power / 1000")
print("-------------------------------------------------")

for i in range(len(names)):
    print("{0:19s} {1:<7d} {2:<7d} {3:^12d}".format(names[i], speeds[i], weights[i], powers[i]))
    
print()



# Question 1.
dictionaries = []

# Here I am generating 4 dictionaries because I'm too lazy to type them all out.
for i in range(len(speeds)):
    someDict = {
        "name": names[i],
        "speed": speeds[i],
        "weight": weights[i],
        "power": powers[i]
    }
    dictionaries.append(someDict)
    
print("Dict method:")
print("Cat                 Speed   Weight  Power / 1000")
print("-------------------------------------------------")

for entry in dictionaries:
    print("{0:19s} {1:<7d} {2:<7d} {3:^12d}".format(entry["name"], entry["speed"], entry["weight"], entry["power"]))

print()



# Question 2.
# Using for loop:
x = 1

for i in range(5):
    x *= (i + 1)    # offset by 1 to avoid multiplying by 0
    
print(x)


# Using while loop:
y = 1
k = 1
while k <= 5:
    y *= k
    k += 1
    
print(y)


# Using recursion:
def factorial(n, k, acc):
    if k <= 5:
        return factorial(n, k + 1, acc * k)
    else:
        return acc
    
print(factorial(5, 1, 1))
