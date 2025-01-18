s = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(s)

for i in "moon":
  print(i)

t = "life is good"
print("good" in t)

#slicing strings
print()

a = "Hello, World!"
print(a[-6:-2])

#modify strings
print()

b = "Hello, World!"
print(b.split(","),'\n')

#string concatenation

a = "Hello"
b = "World"
c = a + ' ' + b
print(c,'\n')

#format strings

age = 17
txt = f"Most graduate students are {age} years old."
print(txt,'\n')

#escape characters

txt = "We are the so-called \"Vikings\".\nWe're from the north.\n"
print(txt)

#string methods
a = "Water"
print(a.replace('Wa', 'But'))