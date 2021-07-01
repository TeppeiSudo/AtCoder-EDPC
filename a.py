N = int(input())
H = list(map(int, input().split()))

dp = [0]*N
dp[1] = abs(H[1] - H[0])

for n in range(2, N):
    dp[n] = min(dp[n-1]+abs(H[n]-H[n-1]), dp[n-2]+abs(H[n]-H[n-2]))

print(dp[N-1])  # 貰うDP