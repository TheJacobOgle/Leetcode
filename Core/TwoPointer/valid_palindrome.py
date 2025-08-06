class Solution:
    def isPalindrome(self, s: str) -> bool:
        return self.isPalindromeBrute(s)

    def isPalindromeSplit(self, s:str) -> bool:
        clean = [char.lower() for char in s if char.isalnum()]
        return clean == clean[::-1]

    # This works but is slow TC: O(n^2)
    def isPalindromeBrute(self, s: str) -> bool:
        for char in s:
            if not char.isalnum():
                s = s.replace(char, "") # O(n) scans full string -- optimize here

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False

        return True
