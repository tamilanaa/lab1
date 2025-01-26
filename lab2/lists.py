list1 = ["abc", 3, True, 4, "def"]
print(list1)
print(type(list1),'\n')

#access list items

list2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list2[:3],'\n')

#change list items 

list3 = ["cake", "cookie", "chocolate"]
list3[1:2] = ["croissant", "cinnabon"]
print(list3,'\n')

#add list items

list4 = ["aman", "boris", "igor"]
list4.insert(2, "darina")
print(list4,'\n')

#remove list items

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)