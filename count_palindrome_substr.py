class Solution:
    def __init__(self):
        self.count = 0
    def f(self, s, start, end) -> None:
        while start >= 0 and end < len(s) and s[start] == s[end]:
            self.count += 1
            # Expand in both directions
            start -= 1
            end += 1


    def countSubstrings(self, s: str) -> int:
        for i in range(len(s)):
            # find all odd length palindrome with `str[i]` as a midpoint
            self.f(s, i, i)
            # find all even length palindrome with `str[i]` and `str[i+1]` as
            # its midpoints
            self.f(s, i, i + 1)

        return self.count



if __name__ == '__main__':
    solution = Solution()
    print(solution.countSubstrings('aaa'))
