thistuple = ("apple", "banana", "cherry", "apple")
print(thistuple)

#access tuples
print(thistuple[2],'\n')

#update tuples
y = list(thistuple)
y[1] = "kiwi"
thistuple = tuple(y)

print(thistuple,'\n')

#unpack tuple

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#loop tuples
print()

for i in range(len(fruits)):
    print(fruits[i])

#join tuples
print()

mytuple = fruits * 2
print(mytuple)

#methods

print(mytuple.count("apple"))