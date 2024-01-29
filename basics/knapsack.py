def knapsack_01(weights, values, W):
    n = len(weights)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(W + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], values[i - 1] + dp[i - 1][j - weights[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][W]


weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
W = 5

result = knapsack_01(weights, values, W)
print("Maximum value:", result)
