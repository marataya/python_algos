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

def interleave(s: str)-> str:
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

def manacherLongestPalindromeSubstr(s: str) -> str:
    right = 0
    center = 0
    s = interleave(s)
    P = list(map(lambda e: 0, range(len(s))))
    maxP = 0
    max_i = 0
    for i in range(1, len(s)):
        mirror = 2*center - i
        if i + P[mirror] <= right and mirror >= len(s) - i:
            P[i] = P[mirror]
        else:
            plength = get_palindrome_length(s, i)
            P[i] = plength
            if plength > 1:
                center = int(i)
                right = center + plength
            if maxP < plength:
                maxP = plength
                max_i = i
    return s[max_i-maxP:max_i+maxP+1].replace('#','')

if __name__ == '__main__':
    begin = time()
    print(longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"))
    end = time()
    print(f'Brute-force: {(end - begin)*1000} ms')


    begin = time()
    print(manacherLongestPalindromeSubstr("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"))

    end = time()
    print(f'Brute-force: {(end - begin)*1000} ms')
