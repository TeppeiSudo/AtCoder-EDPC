N = int(input())
dp = [[0]*3 for _ in range(N+1)]

for n in range(1, N+1):
    candidate = list(map(int, input().split()))
    
    dp[n][0] = max(dp[n-1][1], dp[n-1][2]) + candidate[0]
    dp[n][1] = max(dp[n-1][0], dp[n-1][2]) + candidate[1]
    dp[n][2] = max(dp[n-1][1], dp[n-1][0]) + candidate[2]

print(max(dp[N]))