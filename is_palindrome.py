# Python function is_palindrome(s) check whether a string is palindrome
def is_palindrome(s):
    s = s.upper()
    length = len(s)
    if s == s[::-1]:
        print("TRUE")
    else:
        print("FALSE")
    return 0
s = input("Enter a String\t")
print(is_palindrome(s))
