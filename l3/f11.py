#functions 1 
#1
def converter(grams):
    print(grams, 'grams is' ,grams * 28.3495231,'ounshes')

grams = float(input("Enter grams: "))
converter(grams)

#2 

def temp(fahr):
    print(fahr,'F is', (5 / 9) * (fahr - 32),'C')

fahr = float(input("Temperature in Fahrenheit: "))
temp(fahr)

#3 

def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return(chickens, rabbits)

a = int(input("heads "))
b = int(input("legs "))
print(*solve(a, b))

#4 

def filter_prime(num):
    prime = []
    for n in num:
        if n < 2:
            continue
        isprime = True
        for i in range(2, n, 1):
            if int(n) % i == 0:
                isprime = False
                break
        if isprime:
            prime.append(n)
    print(*prime)

num = list(map(int, input().split()))
filter_prime(num)


#5 Write a function that accepts string from user and print all permutations of that string.
def permut(s, a = ""):
    if len(s) == 0:
        print(a)
        return
    for i in range(len(s)):
        remaining = s[:i] + s[i+1:]
        permut(remaining, a + s[i])

s = input("Enter a string: ")
permut(s)


