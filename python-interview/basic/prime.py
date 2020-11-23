
def prime_numbers(num):
    def is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    if num > 1:
        for i in range(2, num):
            if is_prime(i):
                yield (i, 'prime')
            else:
                yield (i, 'not prime')
    else:
        print(f'{num} is not a prime number')

print(list(prime_numbers(11)))
