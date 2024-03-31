class Solution:
    def plus0ne(self, n: list[int]) -> list[int]:
        num = int(''.join(map(str, n))) + 1
        result = [int(i) for i in str(num)]
        print(result)


if __name__ == '__main__':
    a = map(int, input(": ").split())
    s = Solution()
    s.plus0ne(a)