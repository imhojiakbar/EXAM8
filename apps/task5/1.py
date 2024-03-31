class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        z = s[-1]
        print(len(z))


if __name__ == '__main__':
    a = input(": ").split()
    s = Solution()
    s.lengthOfLastWord(a)