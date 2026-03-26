#1
def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n - 1)
    print(n, end=" ")

#2
def print_n_to_1(n):
    if n == 0:
        return
    print(n, end=" ")
    print_n_to_1(n - 1)

#3
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

#4
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

#5
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

#6
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

#7
def count_digits(n):
    if n == 0:
        return 1
    return 1 + count_digits(n // 10) if n >= 10 else 1

#8
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)

#9
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

#10
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

#11
def sum_array(arr, n):
    if n == 0:
        return 0
    return arr[n - 1] + sum_array(arr, n - 1)

#12
def max_array(arr, n):
    if n == 1:
        return arr[0]
    return max(arr[n - 1], max_array(arr, n - 1))

#13
def count_occurrences(arr, n, target):
    if n == 0:
        return 0
    return (1 if arr[n - 1] == target else 0) + count_occurrences(arr, n - 1, target)

#14
def linear_search(arr, n, target):
    if n == 0:
        return False
    if arr[n - 1] == target:
        return True
    return linear_search(arr, n - 1, target)

#15
def is_sorted(arr, n):
    if n <= 1:
        return True
    if arr[n - 1] < arr[n - 2]:
        return False
    return is_sorted(arr, n - 1)

#16
def binary_search(arr, left, right, target):
    if left > right:
        return -1
    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, left, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, right, target)