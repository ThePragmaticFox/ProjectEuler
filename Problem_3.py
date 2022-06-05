# Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Complexity:
# Time O(sqrt(n))
# Space O(sqrt(n)) 

class Solution:
    def get(self, n: int) -> int:
        m = 1
        while m ** 2 <= n:
            m += 1
        sieve = [True for _ in range(m+1)]
        p = 2
        while p ** 2 <= m:
            if sieve[p]:
                multiple = p ** 2
                while multiple <= m:
                    sieve[multiple] = False
                    multiple += p
            p += 1
        for i in range(m, 0, -1):
            if sieve[i] and n % i == 0:
                return i
        #print(f"m = {m} sieve = {sieve}")
        return 0

solution = Solution()
print(solution.get(600851475143))

# Complexity:
# Time O(sqrt(n))
# Space O(1)

class Solution2:
    def get(self, n: int) -> int:
        p = 2
        res = p
        while n > 1:
            if n % p == 0:
                res = max(res, p)
            while n % p == 0:
                n /= p
            p += 1
        return res

solution = Solution2()
print(solution.get(600851475143))