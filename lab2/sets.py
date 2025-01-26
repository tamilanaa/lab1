set1 = {"apple", "banana", "cherry", "apple"}
print(set1)

#access set items

print("banana" in set1, '\n')

#add set items

tropical = {"pineapple", "mango", "papaya"}

set1.update(tropical)
print(set1)

#remove set items
print()

set1.discard("banana")
print(set1,'\n')

#loop sets

for x in set1:
  print(x)

#join sets
print()

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)