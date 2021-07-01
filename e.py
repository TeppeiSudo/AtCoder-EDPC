N, W = map(int, input().split())
weight, value = [0]*(N+1), [0]*(N+1)
for n in range(1, N+1):
    weight[n], value[n] = map(int, input().split())

# dp[i][v] = i番目までの品物を価値がv以下になるように選んだときの最小の重さ
V = 10**5
dp = [[10**11]*(V+1) for _ in range(N+1)]
dp[0][0] = 0

for n in range(1, N+1):
    for v in range(V+1):
        if v - value[n] >= 0:
            dp[n][v] = min(dp[n-1][v-value[n]] + weight[n], dp[n-1][v])
        else:
            dp[n][v] = dp[n-1][v]

v = V
while dp[N][v] > W:
    v -= 1
print(v)