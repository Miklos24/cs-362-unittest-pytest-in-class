def isPalindrome(s):
    return s == s[::-1]

if __name__ == '__main__':
    print('Please enter a string: ', '')
    s = input()
    if isPalindrome(s):
        print("'{}' is a palindrome.".format(s))
    else:
        print("'{}' is not a palindrome.".format(s))