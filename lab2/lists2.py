#loop lists
list1 = ["apple", "banana", "cherry"]
for i in list1:
    print(i)

print()

#list comprehesion

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
list2 = [x for x in fruits if "n" in x]

print(list2, '\n')

#sort lists

list3 = [99, 1, 59, 85, 23]
list3.sort(reverse = True)
print(list3, '\n')

#copy lists

fruits = ["apple", "banana", "cherry"]
list4 = fruits.copy()
print(list4,'\n')

#join lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)