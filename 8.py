#Write a function, is_prime, that takes an integer and returns True if
#the number is prime and False if the number is not prime.


n=int(input("Enter a number to check:- "))



def is_prime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return False
                break
            else:
                return True

    else:
       return False

print(is_prime(n))
