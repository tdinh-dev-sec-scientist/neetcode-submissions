class Solution:
    def validPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:

                # Try deleting the left character
                left = l + 1
                right = r

                while left < right and s[left] == s[right]:
                    left += 1
                    right -= 1

                if left >= right:
                    return True

                # Try deleting the right character
                left = l
                right = r - 1

                while left < right and s[left] == s[right]:
                    left += 1
                    right -= 1

                return left >= right

            l += 1
            r -= 1

        return True