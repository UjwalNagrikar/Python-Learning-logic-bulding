# main.py
# LOGIC BUILDING WITH LOOPS

# 1. Print all numbers from 1 to 10 using a loop
print("1. Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)


# 2. Print numbers from 10 down to 1 in reverse order
print("\n2. Numbers from 10 to 1:")
for i in range(10, 0, -1):
    print(i)


# 3. Print all even and odd numbers between 1 and 100
print("\n3. Even and Odd numbers from 1 to 100:")
for i in range(1, 101):
    if i % 2 == 0:
        print("Even number:", i)
    else:
        print("Odd number:", i)


# 4. Print all odd numbers between 1 and 100
print("\n4. Only Odd numbers from 1 to 100:")
for i in range(1, 101):
    if i % 2 != 0:
        print("Odd number:", i)


# 5. Multiplication table
print("\n5. Multiplication Table")
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# 6. Sum of first n natural numbers
print("\n6. Sum of first n natural numbers")
n = int(input("Enter a number: "))
total_sum = 0
for i in range(1, n + 1):
    total_sum += i
print(f"Sum = {total_sum}")


# 7. Sum of even numbers up to n
print("\n7. Sum of even numbers")
n = int(input("Enter a number: "))
total_sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        total_sum += i
print(f"Sum of even numbers = {total_sum}")


# 8. Sum of odd numbers up to n
print("\n8. Sum of odd numbers")
n = int(input("Enter a number: "))
total_sum = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        total_sum += i
print(f"Sum of odd numbers = {total_sum}")


# 9. Factorial of a number (using recursion)
print("\n9. Factorial")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number: "))
print(f"Factorial = {factorial(num)}")


# 10. Product of digits of a number
print("\n10. Product of digits")

num = int(input("Enter a number: "))
product = 1

while num > 0:
    digit = num % 10
    product *= digit
    num = num // 10

print("Product of digits:", product)