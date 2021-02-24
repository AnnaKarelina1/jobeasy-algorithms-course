# # Homework1
from random import randint, random
#
#
def rand(n):
    min = pow(10, n-1)
    max = pow(10, n) - 1
    return randint(min, max)

def sum_rand(n):
    result = 0
    while n > 0:
        a = n % 10
        result = result + a
        n = n//10
    return result
#
#
def main():
    number = int(input('enter any number'))
    number_ = rand(number)
    print(number_)
    print (sum_rand(number_))

main()

# # Homework2

a = int(input('number_a:'))
b = int(input('number_b:'))
c = int(input('number_c:'))

if a>=b and a>=c:
    max = a
elif b>=a and b>=c:
    max = b
else:
    max = c
print(max)


#Homework3

def separate(n):
    digits=[]
    while n>0:
        a=n % 10
        digits.append(a)
        n = n // 10
    return digits

def count(n):
    odd=0
    even=0
    n=separate(n)
    for x in n:
        if x % 2==0:
            even+=1
        else:
            odd+=1
    print(odd,even)

# finding the count of odd and even numbers

n = int(input("Enter your number: "))
count(n)






