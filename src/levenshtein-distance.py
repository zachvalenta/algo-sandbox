def levenshtein_distance(s1: str, s2: str) -> int:
    """
    Compute the Levenshtein distance between two strings.

    :param s1: First string
    :param s2: Second string
    :return: Levenshtein distance
    """
    # Initialize matrix with size (len(s1)+1) x (len(s2)+1)
    rows, cols = len(s1) + 1, len(s2) + 1
    dp = [[0] * cols for _ in range(rows)]

    # Fill the first row and column with indices
    for i in range(rows):
        dp[i][0] = i
    for j in range(cols):
        dp[0][j] = j

    # Fill the rest of the matrix
    for i in range(1, rows):
        for j in range(1, cols):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,    # Deletion
                dp[i][j - 1] + 1,    # Insertion
                dp[i - 1][j - 1] + cost  # Substitution
            )

    return dp[-1][-1]


# Example usage
if __name__ == "__main__":
    str1 = "kitten"
    str2 = "sitting"
    distance = levenshtein_distance(str1, str2)
    print(f"Levenshtein distance between '{str1}' and '{str2}': {distance}")
