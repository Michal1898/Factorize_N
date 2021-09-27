def factorize(n):
    prime_numbers = [2]
    for tested_number in range(3, n + 1):
        is_prime = True
        for divisor in prime_numbers:
            if tested_number % divisor == 0:
                is_prime = False

        if is_prime:
            prime_numbers.append(tested_number)

    #print(prime_numbers)
    dividend = n
    divisors = []
    # number_decomposition = f"{n} ="
    number_decomposition = "%s =" % (n)
    while dividend > 1:
        for prime in list(filter(lambda x: x <= dividend, prime_numbers)):
            if dividend % prime == 0:
                divisors.append(prime)
                dividend = int(dividend / prime)
                break

        while len(divisors):
            number_decomposition += " %s *" % (divisors.pop(0))

    number_decomposition = number_decomposition[:-1]
    print(number_decomposition)


if __name__ == "__main__":
    factorize(100000)
    factorize(19)
    factorize(75)
    factorize(1001)
