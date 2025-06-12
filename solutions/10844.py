import sys

n = int(sys.stdin.readline())

dp = [[0] * 10 for _ in range(n + 1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j - 1 >= 0:
            dp[i][j] += dp[i - 1][j - 1] % 1e9

        if j + 1 <= 9:
            dp[i][j] += dp[i - 1][j + 1] % 1e9

print(int(sum(dp[n]) % 1e9))
