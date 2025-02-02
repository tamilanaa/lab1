#6 Write a function that accepts string from user, return a sentence with the words reversed.
# We are ready -> ready are We
def revers(s):
    words = s.split()
    words = words[::-1]
    print(*words)
    
s = input("enter a string: ")
revers(s)

#7 Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

nums = list(map(int, input().split()))
print(has_33(nums))

#8 write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 0 & nums[i + 1] == 0 and nums[i + 2] == 7:
            return True
    return False
    
nums = list(map(int, input().split()))
print(spy_game(nums))

#9 Write a function that computes the volume of a sphere given its radius.
from math import pi
def vol(r):
    return (4/3 * pi * pow(r, 3))
r = int(input())
print("Volume is",round(vol(r), 3))

#10 Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Note: don't use collection set.
def uni(s):
    uniq = []
    for i in s:
        if i not in uniq:
            uniq.append(i)
    print(*uniq)

s = input().split()
uni(s)


#11 palindrome
def papapa(num):
    if num == num[::-1]:
        return("is a palindrome")
    return ("not a palindrome")
a = input()
print(papapa(a))

#12 histogram
def histogram(s):
    for i in s:
        print('*' * int(i))
s = input().split()
histogram(s)

#13 guess
from random import *

def guessnum():

    print("I am thinking of a number between 1 and 20.")
    
    num = randint(1, 20)
    guesses = 0
    
    while True:
        print("Take a guess.")
        guess = int(input())  
        
        guesses += 1
        
        if guess < num:
            print("Your guess is too low.")
        elif guess > num:
            print("Your guess is too high.")
        else:
            print(f"You guessed my number in {guesses} guesses")
            break  

guessnum()
