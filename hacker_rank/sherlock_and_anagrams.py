"""

"""


def sherlockAndAnagrams(s):
    # Initialize a dictionary to store the frequency of substrings
    freq = {}
    n = len(s)
    result = 0

    for length in range(1, n):
        for i in range(n - length + 1):
            substr = ''.join(sorted(s[i:i+length]))
            if substr in freq:
                freq[substr] += 1
            else:
                freq[substr] = 1

    for freq in freq.values():
        result += freq * (freq - 1) // 2

    return result


if __name__ == '__main__':
    # Sample Input
    queries = ['ifailuhkqq', 'kkkk']

    # Output the count of anagram pairs for each query
    for query in queries:
        print(sherlockAndAnagrams(query))
