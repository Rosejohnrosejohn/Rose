def is_palindrome(s):
    return s == s[::-1]

# Example usage
test_string = "malayalam"
print(f"{test_string} is a palindrome: {is_palindrome(test_string)}")
