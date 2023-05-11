n, s = [int(i) for i in input().split()]
arr = [int(input()) for i in range(n)]
dp = [[0 for i in range(s + 1)] for j in range(n + 1)]

for i in dp:
    i[0] = 1
for i in range(1, n + 1):
    for j in range(1, s + 1):
        if j < arr[i - 1]:
            dp[i][j] = dp[i - 1][j]
        else:
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j - arr[i - 1]]
if dp[n][s]:
    print("Yes")
else:
    print("No")
