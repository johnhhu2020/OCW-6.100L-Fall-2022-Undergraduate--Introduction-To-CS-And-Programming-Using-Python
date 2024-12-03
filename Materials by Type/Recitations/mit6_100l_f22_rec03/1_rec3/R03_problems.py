# Problem 1 - Bisection Search Practise
# Write a program using bisection search to find the forth root of a number inputted by the 
# user. Print the forth root calculated with max error of 0.01. 

x = float(input("Using bisection search calculate the forth root of: " ))
epsilon = 0.01
low = 0
high = x
ans = (low + high)/2

while abs(ans**4 - x) > epsilon:
    if ans**4 > x:
        high = ans
    else:
        low = ans
    ans = (low + high)/2
print(f"{ans} is probabily your answer")




# Problem 2 - Functions 
# Write a Python function to check whether a number falls in a given range. 
def num_range_check(x, a, b):
    '''
    x: a number to be checked
    a, b: the range, lower to higher
    return Trus if a lies between a and b'''
    return a <= x and x <= b

result = num_range_check(3,2,8)
result = num_range_check(2,3,8)
print(result)



# Problem 3 - Functions 
# Write a Python function to check whether a number is perfect or not.
# (In number theory, a perfect number is a positive integer that is equal 
# to the sum of its proper positive divisors, excluding the number itself).
def perfect_num_check(x):
    sum_it = []
    for i in range(1, x):
        if x%i == 0:
            sum_it.append(i)
    print(sum_it)
    return x == sum(sum_it)

check1 = perfect_num_check(6)
print(f"check1 6 perfect or not: {check1}")
check2 = perfect_num_check(28)
print(f"check2 28 perfect or not: {check2}")
check3 = perfect_num_check(29)
print(f"check3 29 perfect or not: {check3}")




# Problem 4 - Approximation Algorithm (see Lecture 5 slides for similar problem)
# Write an approximation algorithm to calculate the forth root of some 
# number inputted by the user. 
# Print the result and the number of iterations required to reach that result. 
# The program should not accept negative numbers. Initial parameters epsilon 
# (i.e. accuracy), initial guess, increment and num_guesses are defined below.

# example initial parameters
epsilon = 0.01
ans = 0.0
increment = 0.001
num_guesses = 0

### I forgot what is the Approximation Algorithm ###
x = int(input("Please give me a positive number to guess its 4th root: "))
ans = ans + increment
if x <= 0:
    print(f"Error {x}, please provide a Positive Number")
else:
    pass
while abs(ans**4 - x) > epsilon:
    ans += increment
    num_guesses += 1
print(f"the 4th root of your positive number: {x} is probabily: {ans}, and it takes {num_guesses} guesses")

