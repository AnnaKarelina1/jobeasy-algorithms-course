def sum_divisors(n):
    result=0
    for i in range(1,n):
        if n%i==0:
            result+=i
    return result


def compare_sum(n1,n2):
    if sum_divisors(n1)==n2 and sum_divisors(n2)==n1:
        print(sum_divisors(n1))
        print(sum_divisors(n2))
        return "The numbers are amicable!"
    else:
        return "Try again!"

print(compare_sum(220,284))