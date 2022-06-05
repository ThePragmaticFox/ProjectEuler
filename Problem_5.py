# Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Complexity:
# Time O(n * log(n!)), n is the input, n! is if you would multiply together from 2 to n (so obviously it's lower than that).
# Space O(n), due to recursive stack trace, though that can be avoided without any issues.

class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a%b)

    def lcm(self, a, b):
        return a*b//self.gcd(a,b)

    def get(self, n: int) -> int:
        res = 1
        for i in range(2, n+1):
            res = self.lcm(res, i)
        return res

solution = Solution()
print(solution.get(20))