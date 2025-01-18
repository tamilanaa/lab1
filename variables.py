x = 5
y = "Zima"
print(type(x))
print(x)
print(type(y))

#variable names
print()

myname = "Tamilana"
my_name = "Tamila"
_my_name = "Tami"
MyName = "Tam"
MYVNAME = "Ta"
myname3 = "T"

#miltiple values

x, y, z = "fish", "bird", "insect"
print(x)
print(y)
print(z,'\n')

#output variables

x = "Roses "
y = "are "
z = "red"
print(x + y + z,'\n')

#global variables

x = "purple"

def fun():
  x = "blue"
  print("Violets are " + x)

fun()

print("Violets are " + x)

