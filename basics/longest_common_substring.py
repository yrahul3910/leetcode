def longest_common_substring(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_len, end_pos = 0, 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_pos = i
            else:
                dp[i][j] = 0

    # Reconstruct the LCS
    lcs = str1[end_pos - max_len:end_pos]

    return lcs

# Example usage:
str1 = "ABABC"
str2 = "BABCBA"
result = longest_common_substring(str1, str2)
print("Longest Common Substring:", result)

