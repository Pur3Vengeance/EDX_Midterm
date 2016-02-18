#Accepts positive integer n and returns sorted list in ascending order
#of all prime numbers between 2 and n but not including 2 and n.
#A prime number is a number that has no other divisors except 1 and itself

def list_of_primes(num):

    for x in range(1,num):

        y = 3

        if x%2 ==0:
           del x
        else:
            for y in range(1,num):
                if x%y ==0:
                    del x
        print (x)




list_of_primes(200)
