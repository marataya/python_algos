def is_palindrome(s: str) -> bool:
    n = len(s)
    if n <= 1 or (s[0] == s[-1] and is_palindrome(s[1:-1])):
        return True
    return False

if __name__ == '__main__':
    print(is_palindrome('racecar'))


