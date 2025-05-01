class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        copPal = palindrome
        if len(palindrome) == 1:
            return ""
        for i in palindrome:
            if i != "a":
                palindrome = palindrome.replace(i, "a", 1)
                if palindrome == palindrome[::-1]:
                    palindrome = copPal
                    continue
                else:
                    return palindrome
        palindrome = palindrome[:-1] + "b"
        return palindrome