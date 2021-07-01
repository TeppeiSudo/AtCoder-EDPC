s = str(input())
t = str(input())

dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
for i in range(1, len(s)+1):
    for j in range(1, len(t)+1):
        if s[i-1] == t[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


i = len(s)
j = len(t)
length = dp[i][j]
ans = [""]*length
while length > 0:
    if s[i-1] == t[j-1]:
        ans[length-1] = s[i-1]
        i -= 1
        j -= 1
        length -= 1
    elif dp[i][j] == dp[i-1][j]:
        i -= 1
    else:
        j -= 1

print("".join(ans))