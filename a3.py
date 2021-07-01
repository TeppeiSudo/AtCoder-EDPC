N = int(input())
H = list(map(int, input().split()))

dp = [10**9]*N
dp[1] = abs(H[1] - H[0])
dp[0] = 0

def recdp(n):
    if dp[n] != 10**9:
        return dp[n]
    else:
        dp[n] = min(recdp(n-1)+abs(H[n]-H[n-1]), recdp(n-2)+abs(H[n]-H[n-2]))
        return dp[n]

print(recdp(N-1))  # メモ化再帰