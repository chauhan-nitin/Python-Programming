#Python function named sqrt_newton(num) that implements Newton's method to compute the square root
def sqrt_newton(num):
    guess = num/2
    while (guess**2-num)>10**-12:
        guess = (guess + num/guess) * 0.5
    return guess
#Creating a variable num that is assigned a non-negative number entered by the user
num = int(input("Enter a non-negative number\t"))
print(sqrt_newton(num))
