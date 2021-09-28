def factorize(n):
    dividend = n
    divisors = []
    number_decomposition = "%s =" % (n)
    while dividend > 1:
        for prime in range(2, dividend + 1):
            if dividend % prime == 0:
                divisors.append(prime)
                dividend = int(dividend / prime)
                break

        while len(divisors):
            number_decomposition += " %s *" % (divisors.pop(0))

    number_decomposition = number_decomposition[:-2]
    print(number_decomposition)


if __name__ == "__main__":
    for my_number in range(2, 10002):
        factorize(my_number)
