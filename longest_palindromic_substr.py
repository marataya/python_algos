from time import time


def longestPalindrome(s: str) -> str:
    if len(s) <= 1:
        return s
    longest_palindrome = s[0]
    for i in range(0, len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                if len(longest_palindrome) < len(substring):
                    longest_palindrome = substring

    return longest_palindrome


def interleave(s: str) -> str:
    result = []
    for el in s:
        result.extend(['#', el])
    result.append('#')
    return ''.join(result)


def get_palindrome_length(string, index):
    """
    Returns length of longest palindromic substring centered in the given index.
    """
    length = 1
    while index + length < len(string) and index - length >= 0:
        if string[index + length] == string[index - length]:
            length += 1
        else:
            break

    return length - 1


def manacherLongestPalindromeSubstr(seq: str) -> str:
    """
    Behaves identically to naiveLongestPalindrome (see below), but
    runs in linear time.
    """
    seqLen = len(seq)
    l = []
    i = 0
    palLen = 0
    # Loop invariant: seq[(i - palLen):i] is a palindrome.
    # Loop invariant: len(l) >= 2 * i - palLen. The code path that
    # increments palLen skips the l-filling inner-loop.
    # Loop invariant: len(l) < 2 * i + 1. Any code path that
    # increments i past seqLen - 1 exits the loop early and so skips
    # the l-filling inner loop.
    while i < seqLen:
        # First, see if we can extend the current palindrome.  Note
        # that the center of the palindrome remains fixed.
        if i > palLen and seq[i - palLen - 1] == seq[i]:
            palLen += 2
            i += 1
            continue

        # The current palindrome is as large as it gets, so we append
        # it.
        l.append(palLen)

        # Now to make further progress, we look for a smaller
        # palindrome sharing the right edge with the current
        # palindrome.  If we find one, we can try to expand it and see
        # where that takes us.  At the same time, we can fill the
        # values for l that we neglected during the loop above. We
        # make use of our knowledge of the length of the previous
        # palindrome (palLen) and the fact that the values of l for
        # positions on the right half of the palindrome are closely
        # related to the values of the corresponding positions on the
        # left half of the palindrome.

        # Traverse backwards starting from the second-to-last index up
        # to the edge of the last palindrome.
        s = len(l) - 2
        e = s - palLen
        for j in range(s, e, -1):
            # d is the value l[j] must have in order for the
            # palindrome centered there to share the left edge with
            # the last palindrome.  (Drawing it out is helpful to
            # understanding why the - 1 is there.)
            d = j - e - 1

            # We check to see if the palindrome at l[j] shares a left
            # edge with the last palindrome.  If so, the corresponding
            # palindrome on the right half must share the right edge
            # with the last palindrome, and so we have a new value for
            # palLen.
            #
            # An exercise for the reader: in this place in the code you
            # might think that you can replace the == with >= to improve
            # performance.  This does not change the correctness of the
            # algorithm but it does hurt performance, contrary to
            # expectations.  Why?
            if l[j] == d:
                palLen = d
                # We actually want to go to the beginning of the outer
                # loop, but Python doesn't have loop labels.  Instead,
                # we use an else block corresponding to the inner
                # loop, which gets executed only when the for loop
                # exits normally (i.e., not via break).
                break

            # Otherwise, we just copy the value over to the right
            # side.  We have to bound l[i] because palindromes on the
            # left side could extend past the left edge of the last
            # palindrome, whereas their counterparts won't extend past
            # the right edge.
            l.append(min(d, l[j]))
        else:
            # This code is executed in two cases: when the for loop
            # isn't taken at all (palLen == 0) or the inner loop was
            # unable to find a palindrome sharing the left edge with
            # the last palindrome.  In either case, we're free to
            # consider the palindrome centered at seq[i].
            palLen = 1
            i += 1

    # We know from the loop invariant that len(l) < 2 * seqLen + 1, so
    # we must fill in the remaining values of l.

    # Obviously, the last palindrome we're looking at can't grow any
    # more.
    l.append(palLen)

    # Traverse backwards starting from the second-to-last index up
    # until we get l to size 2 * seqLen + 1. We can deduce from the
    # loop invariants we have enough elements.
    lLen = len(l)
    s = lLen - 2
    e = s - (2 * seqLen + 1 - lLen)
    for i in range(s, e, -1):
        # The d here uses the same formula as the d in the inner loop
        # above.  (Computes distance to left edge of the last
        # palindrome.)
        d = i - e - 1
        # We bound l[i] with min for the same reason as in the inner
        # loop above.
        l.append(min(d, l[i]))
    max = 0
    max_i = 0
    for i in range(len(l)):
        if max < l[i]:
            max = l[i]
            max_i = i
    resultStr = interleave(seq)
    return resultStr[max_i - max : max_i + max+1].replace('#', '')


'''
Intuition
Using Manacher's algorithm to find the longest palindromic substring efficiently.

Approach
1 String Transformation: The input string 's' is transformed into a new string 'modified_s' by inserting special characters ('#') between each character and at the beginning and end. This transformation allows the algorithm to handle both even and odd-length palindromes in the same way.

2 Initialization: Initialize variables to keep track of the current center 'C' and the right boundary 'R' of the current palindrome. Also, initialize variables to store the maximum length of a palindrome found ('max_len') and its center ('max_center').

3 Palindromic Length Array: Create an array 'P' to store the length of palindromes at each position in the 'modified_s' string. Initialize it with zeros.

4 Loop through the String: Iterate through the characters of 'modified_s'. For each character 'modified_s[i]', do the following:

- If 'i' is within the right boundary 'R', calculate the mirror position 'mirror' of 'i' with respect to the center 'C'. Update 'P[i]' as the minimum of the remaining length of the current palindrome ('R - i') and the corresponding value in 'P[mirror]'. This step takes advantage of known palindromes to avoid redundant computations.
- Expand around 'i': Check if the characters at positions 'a' and 'b' are the same, where 'a' is the position one character to the right and 'b' is one character to the left of 'i'. While the characters at 'a' and 'b' match and are within the bounds of the string, increment 'P[i]' and move 'a' and 'b' outwards.
- Update the center and right boundary: If 'i + P[i]' exceeds the right boundary 'R', update 'C' and 'R' to 'i' and 'i + P[i]' to represent the new center and right boundary of the current palindrome.
- Update the maximum length: If 'P[i]' is greater than 'max_len', update 'max_len' and 'max_center' to 'P[i]' and 'i', respectively.
5 Find the Longest Palindromic Substring: After the loop, calculate the start and end indices of the longest palindromic substring by using the 'max_len' and 'max_center'. The start index is calculated as (max_center - max_len) // 2, and the end index is 'start + max_len'.

6 Return the Result: Return the longest palindromic substring by extracting the substring from 's' using the start and end indices.

Complexity
Time complexity: O(n)O(n)O(n)
Space complexity: O(n)O(n)O(n)

'''
def manacherAlgo2(s: str) -> str:
    modified_s = "#"
    for char in s:
        modified_s += char + "#"

    n = len(modified_s)
    P = [0] * n  # Array to store the length of palindromes at each position
    C, R = 0, 0  # Center and right boundary of the current palindrome

    max_len = 0  # Maximum length of a palindrome found
    max_center = 0  # Center of the palindrome with maximum length

    for i in range(n):
        if i < R:
            mirror = 2 * C - i  # Mirror position of i
            P[i] = min(R - i, P[mirror])

        # Expand around the current character
        a, b = i + (1 + P[i]), i - (1 + P[i])
        while a < n and b >= 0 and modified_s[a] == modified_s[b]:
            P[i] += 1
            a += 1
            b -= 1

        # Update the center and right boundary if needed
        if i + P[i] > R:
            C, R = i, i + P[i]

        # Update the maximum length and its center
        if P[i] > max_len:
            max_len = P[i]
            max_center = i

    start = (max_center - max_len) // 2  # Start index of the longest palindrome
    end = start + max_len  # End index of the longest palindrome

    return s[start:end]

'''
O(n^2) solution using
'''
def naiveLongestPalindromes(seq):
    """
    Given a sequence seq, returns a list l such that l[2 * i + 1]
    holds the length of the longest palindrome centered at seq[i]
    (which must be odd), l[2 * i] holds the length of the longest
    palindrome centered between seq[i - 1] and seq[i] (which must be
    even), and l[2 * len(seq)] holds the length of the longest
    palindrome centered past the last element of seq (which must be 0,
    as is l[0]).

    The actual palindrome for l[i] is seq[s:(s + l[i])] where s is i
    // 2 - l[i] // 2. (// is integer division.)

    Example:
    naiveLongestPalindrome('ababa') -> [0, 1, 0, 3, 0, 5, 0, 3, 0, 1]

    Runs in quadratic time.
    """
    seqLen = len(seq)
    lLen = 2 * seqLen + 1
    l = []

    for i in range(lLen):
        # If i is even (i.e., we're on a space), this will produce e
        # == s.  Otherwise, we're on an element and e == s + 1, as a
        # single letter is trivially a palindrome.
        s = i // 2
        e = s + i % 2

        # Loop invariant: seq[s:e] is a palindrome.
        while s > 0 and e < seqLen and seq[s - 1] == seq[e]:
            s -= 1
            e += 1

        l.append(e - s)
    max = 0
    max_i = 0
    for i in range(len(l)):
        if max < l[i]:
            max = l[i]
            max_i = i
    resultStr = interleave(seq)
    return resultStr[max_i - max : max_i + max+1].replace('#', '')

if __name__ == '__main__':
    # begin = time()
    # print(longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"))
    # end = time()
    # print(f'Brute-force: {(end - begin)*1000} ms')
    #

    begin = time()
    print(manacherLongestPalindromeSubstr("cvvd"))

    end = time()
    print(f'Brute-force: {(end - begin) * 1000} ms')

    begin = time()
    print(naiveLongestPalindromes("cvvd"))

    end = time()
    print(f'Brute-force: {(end - begin) * 1000} ms')
