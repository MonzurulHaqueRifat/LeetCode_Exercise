class Solution:
    def isPalindrome(self, s: str):
        s = s.lower()
        s = ''.join(ch for ch in s if ch.isalnum())
        # print(s)
        start = 0
        end = len(s) - 1
        while (start < end):
            if (s[start] != s[end]):
                return False
            else:
                start += 1
                end -= 1
        return True

