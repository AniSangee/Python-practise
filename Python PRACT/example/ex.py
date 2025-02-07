def is_palindrome(s):
    s=s.lower().replace("","")
    return s==reversed(s)

word = input("Enter the word:")
if is_palindrome(word):
    print("Is palindrome word.")
else:
    print("Is not palindrome.")