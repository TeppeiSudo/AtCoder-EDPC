N, W = map(int, input().split())
weight, value = [0]*(N+1), [0]*(N+1)
for n in range(1, N+1):
    weight[n], value[n] = map(int, input().split())

# dp[i][w] = i番目までの品物を重さw以下になるように選んだときの最大価値
dp = [[0]*(W+1) for _ in range(N+1)]

for n in range(1, N+1):
    for w in range(1, W+1):
        if w-weight[n] >= 0:
            dp[n][w] = max(dp[n-1][w-weight[n]] + value[n], dp[n-1][w])
        else:
            dp[n][w] = dp[n-1][w]

print(dp[N][W])