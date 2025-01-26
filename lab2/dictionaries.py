thisdict = {
  "model": "Student",
  "year": 2006
}
print(thisdict["model"],'\n')

#access items

x = thisdict.get("year")
print(x)

#change items

thisdict["year"] = 2007
print(thisdict["year"])

print()
#add ilems

thisdict.update({"Speciality": "IS"})
print(thisdict)

#remove items

thisdict.popitem()
print(thisdict)

#loop dictionaries
print()

for x in thisdict:
    print(x)

#copy dictionaries
print()

mydict = thisdict.copy()
print(mydict)

print()
#nested dictionaries

child1 = {
  "name" : "Eldar",
  "year" : 2003
}
child2 = {
  "name" : "Tamilana",
  "year" : 2006
}


myfamily = {
  "child1" : child1,
  "child2" : child2,
}
print(myfamily)

