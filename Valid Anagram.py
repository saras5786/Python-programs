class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)


# This part runs only in IDLE / local environment
if __name__ == "__main__":
    s = input("Enter first string: ")
    t = input("Enter second string: ")

    obj = Solution()
    print("Is Anagram:", obj.isAnagram(s, t))
