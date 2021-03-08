

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

number = int(input("Number:"))


if number <= 0:
   print("Number should be > 0")
else:
   print("Fibonacci sequence:")
   for i in range(number):
       print(recur_fibo(i))




def recur_factor(n):
    if n<2:
        return 1
    else:
        return n*recur_factor(n-1)

number=int(input("Number: "))

for i in range(number):
        print(recur_factor(i))



def recur_sum_number(n):
    if n < 10:
        return n
    n = n % 10 + recur_sum_number(n // 10)
    return recur_sum_number(n)

n=int(input("Number:"))
print(recur_sum_number(n))