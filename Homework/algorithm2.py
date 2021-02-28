# Fiboanacci
# # # TODO: HW: Rewrite code, which will return only needed element of Fib sequence
# def fib_seq(n):
#     if n==0:
#         return[0]
#     elif n==1:
#         return[1]
#     elif n==2:
#         return [1, 1]
#     f_1=1
#     f_2=1
#     fibonacci=[f_1, f_2, 2]
#     while n>2:
#         f_1, f_2 = f_2, f_1 + f_2
#         fibonacci.append(f_1+f_2)
#         n-=1
#     return fibonacci
#
# number=int(input("Enter the number: "))
# print(fib_seq(number))

def Fibonacci(n):
    if n < 0:
        print("Incorrect number")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

n=int(input("Enter your number: "))
print(Fibonacci(n))

#
#
#
# #
# # Zeros not for Heros
# # Numbers ending with zeros are boring. They might be fun in your world, but not here. Get rid of them. Only the ending ones.
# #
# # # 1450 -> 145
# # # 960000 -> 96
# # # 1050 -> 105
# # # -1050 -> -105
# # # Zero alone is fine, don't worry about it. Poor guy anyway
#
def remove_zero(n):
    n=str(n)
    while True:
        if n[-1]=='0':
            n = n[:-1]
        elif n[-1]!='0':
            print(n)
            break
#
# number=int(input("Enter your number: "))
# remove_zero(number)
#
# #
# # Digital root is the recursive sum of all the digits in a number.
# # # Given n, take the sum of the digits of n.
# # # If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
# # # This is only applicable to the natural numbers.
# #
# # # 16  -->  1 + 6 = 7
# # # 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# # # 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# # # 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
#
def sum_number(n):
    sum=0
    while n>0 or sum>9:
        if n==0:
            n=sum
            sum=0
        sum+=n%10
        n=n//10
    return sum
#
#
number=int(input("Enter the number: "))
print (sum_number(number))