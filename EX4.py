#Accepts positive integer n and returns sorted list in ascending order
#of all prime numbers between 2 and n but not including 2 and n.
#A prime number is a number that has no other divisors except 1 and itself

def list_of_primes(n):

    for number in range(1,n+1):

        divider = 1
        primes = []

        if number%divider ==0:
            primes.append(number)
            divider = divider + 1
        print(primes)

            




list_of_primes(200)
