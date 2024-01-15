def vowels_consonants(s: str) -> int:
    vowels = ['a','e','o','i','u', 'y']
    n = len(s)
    if n == 0:
        return 0
    if n == 1:
        if s in vowels:
            return 1
        else:
            return -1
    if s[0] in vowels:
        return has_more_vowels_than_consonants(s[1:]) + 1
    else:
        return has_more_vowels_than_consonants(s[1:]) - 1

def has_more_vowels_than_consonants(s: str) -> int:
    if vowels_consonants(s) > 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print(has_more_vowels_than_consonants('ba'))
