def longest_palindromic_substring(s):
    """
    Given a string s, return the longest palindromic substring.
    """
    if not s:
        return ""

    n = len(s)
    start = 0
    max_length = 1

    def expand(left, right):
        nonlocal start, max_length
        while left >= 0 and right < n and s[left] == s[right]:
            current_length = right - left + 1
            if current_length > max_length:
                max_length = current_length
                start = left
            left -= 1
            right += 1

    for i in range(n):
        expand(i, i)
        expand(i, i + 1)

    return s[start:start + max_length]