
#Basic Python File For Docking
#Idea(Goal): Creating Container Image for this Code
import os

num = int(os.getenv("N","1"))
num1=num
fact=1
while num >= 1:
    fact *= num
    num -= 1
print(f"Factorial of {num1}:{fact}")
