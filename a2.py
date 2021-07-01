N = int(input())
H = list(map(int, input().split()))

dp = [10**9]*N
dp[0] = 0

for n in range(N-1):
    dp[n+1] = min(dp[n+1], dp[n]+abs(H[n+1]-H[n]))
    if n+2 < N:
        dp[n+2] = min(dp[n+2], dp[n]+abs(H[n+2]-H[n]))

print(dp[N-1])  # 配るDP