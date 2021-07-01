N, K = map(int, input().split())
H = list(map(int, input().split()))

dp = [0]*N
dp[1] = abs(H[1] - H[0])

for n in range(2, N):
    costs = [dp[n-i]+abs(H[n]-H[n-i]) for i in range(1, min(n+1,K+1))]
    dp[n] = min(costs)

print(dp[N-1])  # 貰うDP