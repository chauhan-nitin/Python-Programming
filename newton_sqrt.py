#Python function named sqrt_newton(x) that implements Newton's method to compute the square root
def sqrt_newton(x):
    guess = x/2
    while (guess**2-x)>10**-12:
        guess = (guess + x/guess) * 0.5
    return guess
x = int(input("Enter a non-negative number\t"))
print(sqrt_newton(x))
