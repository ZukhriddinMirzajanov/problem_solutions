import numpy as np

# numbers = np.array([1, 4, 5, 7, 9, 11])

# N.1 How to find the missing numbers in an integer array of 1 to 10?

# def missing_numbers(arr):
#     count = 0
#     for i in range(len(arr)):
#         if i >= 1:
#             count += 1
#             if count != arr[i]:
#                 print(count)
#                 dif = arr[i] - count
#                 for i in range(dif-1):
#                     count += 1
#                     print(count)
#                 count += 1
#             # print(count)
#         else:
#             count = arr[i]


# N.2 How to find the missing number in an integer array of 1 to 10?
# arr = [1, 2, 3, 4, 5, 6, 8, 9, 10]


# def missing_number(arr, n):
#     sum1 = n*(n+1)/2
#     sum2 = sum(arr)
#     print(sum1-sum2)


# N.3 Write a program to find all pairs of integers whose given
# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# def find_pairs(arr, number):
#     for i in arr:
#         for j in arr:
#             if (i + j) == number and i != j:
#                 print([i, j])


# N:4 How to find maximum number of two integers in the array where all elemnts are positive
# numbers = np.array([1, 12, 20, 32, 44, 48, 5, 56, -57, 39, -60])


# def find_two_max1(arr):
#     a = arr[0]
#     for i in arr:
#         if i >= a:
#             a = i
#     b = arr[0]
#     for i in arr:
#         if i >= b and i != a:
#             b = i
#     print(a, b)


# def find_two_max2(arr):
#     a, b = 0, 0
#     for i in arr:
#         for j in arr:
#             if i * j > a*b and i != j:
#                 a, b = i, j
#     print(a, b)

# N:5 Implement an algorithm to determine if a list has all unique characters, using python list
# my_list = [1, 3, 5, 7, 8, 9, 18, 10]


# def is_unique(arr):
#     a = arr[0]
#     count = 0
#     for i in arr:
#         for j in arr:
#             if i == j:
#                 count += 1
#         if count > 1:
#             print(False)
#             break
#         count = 0
#     if count < 1:
#         print(True)


# def permutation(a, b):
#     if len(a) == len(b):
#         c = []
#         count = 0
#         for i in a:
#             for j in b:
#                 if i == j and count == 0:
#                     c.append(i)
#                     count += 1
#             count = 0
#         if len(c) == len(a):
#             print(True)
#         else:
#             print(False)
#     else:
#         print(False)

# N: Given an image represented by an NxN matrix write a method to rotate the image by 90 degrees.

# matrix1 = np.array([[1, 2, 3], [4, 5, 6, ], [7, 8, 9]])
# matrix2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
#                     [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
# matrix[0][0], matrix[0][3], matrix[3][3], matrix[3][0] = matrix[3][0], matrix[0][0], matrix[0][3], matrix[3][3]
# print(matrix)


# def rotate_matrix(matrix):
#     it = 0
#     a = len(matrix)-1
#     b = len(matrix[0])-1
#     while b >= 2:
#         matrix[it][it], matrix[it][b], matrix[a][b], matrix[a][it] = matrix[a][it], matrix[it][it], matrix[it][b], matrix[a][b]
#         a1 = a
#         b1 = b

#         for i in range(it, b-1):

#             a1 -= 1
#             b1 -= 1
#             matrix[i+1][it], matrix[it][b1], matrix[a1][b], matrix[a][i +
#                                                                       1] = matrix[a][i+1], matrix[i+1][it], matrix[it][b1], matrix[a1][b]
#             print(a1, b1)

#         it += 1
#         b -= 1
#         a -= 1
#     print(matrix)


# def rotate_matrix2(matrix):
#     n = len(matrix)
#     for i in range(n//2):
#         first = i
#         last = n - i - 1
#         for j in range(first, last):
#             top = matrix[i][j]
#             matrix[i][j] = matrix[-j-1][i]
#             matrix[-j-1][i] = matrix[-i-1][-j-1]
#             matrix[-i-1][-j-1] = matrix[j][-i-1]
#             matrix[j][-i-1] = top

#     print(matrix)
