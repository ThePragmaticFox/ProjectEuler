# Largest palindrome product
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Complexity:
# Time O(((10 ** n) ** 2) * (n ** 2))
# Space O(1)

class Solution:
    def get(self, n: int) -> int:
        low = 10 ** (n-1)
        high = 0
        for i in range(n):
            high += 9 * 10 ** i
        highest = 0
        #print(f"low = {low} high = {high}")
        for a in range(low, high+1, 1):
            for b in range(low, high+1, 1):
                c = a*b
                if c % 10 == 0:
                    continue
                d = 0
                while c > 0:
                    d = d * 10 + (c % 10)
                    c //= 10
                if a*b == d:
                    #print(f"a*b = {a*b} c = {c} d = {d} i = {i}")
                    highest = max(highest, a*b)
        return highest

solution = Solution()
print(solution.get(3))

# Complexity:
# Time O(((10 ** n) ** 2) * (n ** 2))
# Space O(n)

class Solution2:
    def get(self, n: int) -> int:
        low = 10 ** (n-1)
        high = 0
        for i in range(n):
            high += 9 * 10 ** i
        highest = 0
        for a in range(low, high+1, 1):
            for b in range(low, high+1, 1):
                c = str(a*b)
                d = c[::-1]
                if c == d:
                    highest = max(highest, a*b)
        return highest

solution = Solution2()
print(solution.get(3))