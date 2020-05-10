def edit_distance(word1, word2):
    n = len(word1)
    m = len(word2)

    # if one of the strings is empty
    if n * m == 0:
        return n + m

    # array to store the conversion history
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # init boundaries
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    # DP compute
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            left = dp[i - 1][j] + 1
            down = dp[i][j - 1] + 1
            left_down = dp[i - 1][j - 1]
            if word1[i - 1] != word2[j - 1]:
                left_down += 1
            dp[i][j] = min(left, down, left_down)

    return dp[n][m]
