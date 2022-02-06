# def fuctorial(n):
#     assert n >= 0 and int(n) == n, "Only integer"
#     if n in [0, 1]:
#         return 1
#     else:
#         return n * fuctorial(n-1)


# print(fuctorial(4))

# assert n >= 0 and int(n) == n, "Only integer"
# num = 1
# for i in range(1, n+1):
#     num *= i
# print(num)


def fibonacci(n):
    assert n >= 0 and int(n) == n, "Only integer"
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# def sum_of_digits(n):
#     assert n >= 0 and int(n) == n, 'only integer num'
#     if n == 0:
#         return 0
#     else:
#         return int(n % 10) + sum_of_digits(int(n/10))


# def sum1(n):
#     assert n >= 0 and int(n) == n, 'only integer num'
#     n = str(n)
#     a = 0
#     for i in n:
#         a += int(i)
#     return a


# def power(base, exponent):
#     assert exponent >= 0 and int(exponent) == exponent, "error"
#     if exponent == 0:
#         return 1
#     else:
#         return base * power(base, exponent-1)


# def great_common_divisor(num1, num2):
#     assert int(num1) == num1 and int(num2) == num2, "error"
#     if num1 < 0:
#         num1 = -1 * num1
#     if num2 < 0:
#         num2 = -1 * num2
#     if num2 == 0:
#         return num1
#     else:
#         return great_common_divisor(num2, num1 % num2)


# def decimal_to_binary(n):
#     assert n >= 0 and int(n) == n, "error"
#     if n <= 1:
#         return 1
#     else:
#         return n % 2 + 10 * decimal_to_binary(int(n/2))
