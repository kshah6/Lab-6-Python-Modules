# Kunal Shah
# Date 02/08/2022

# Problem 1
#importing the random function
import random

# Using for loop to print 10 random integers
for i in range(10):
    print(random.randrange(25, 36))


# Problem 2

# importing random
import random

# print using randrange function
print(random.randrange(0, 50) * 2 + 1)

# Problem 3

# importing random 
import random

# number of days in a list
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(random.choice(days))


# Problem 4

# importing math library
import math
# intialize denominator
k = 1
# intialize sum
s = 0
for i in range(1000000):
    # even index elements are positive
    if i % 2 == 0:
        s = s + 4 / k

    else:
        # odd index elements are negative
        s = s - 4 / k

    k = k + 2

print("Value of estimated pi: ", s)

# Value of pi
print("Value of pi from math module: ", math.pi)


# Problem 5

# value of pi
pi = 3.14
# enter the radians
radian = int(input("Enter radians: "))
# radians to degree conversion

degree = radian * (180 / pi)
print(degree)


# Problem 6

# importing math function
import math

# input integer value
n = int(input("Enter an integer: "))
result = 1

# using for loop to increment
for i in range(1, n + 1):
    result *= i
print("factorial of {} using for loop: {}".format(n, result))
print("factorial of {} using inbuilt function: {}".format(n, math.factorial(n)))


