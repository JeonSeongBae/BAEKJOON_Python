# -*- Encoding:UTF-8 -*-

# 백준 알고리즘 1912번
# 연속합


N = int(input())
numbers = [int(i) for i in input().split()]
numbers.append(0)
# dp = [0 for i in range(len(numbers))]

max = 0
dp = numbers

for i in range(2, len(dp)):
    if dp[i-1] > 0 and dp[i] + dp[i - 1] > 0:
        dp[i] += dp[i - 1]

    if max < dp[i]:
        max = dp[i]

print(max)

