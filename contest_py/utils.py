from typing import List


def buildZList(s: str) -> List[int]:
    """
    Used in pattern matching: buildZList(needle + '.' + haystack) and check for length(needle) in result

    Construct an array of length equal to the length of the input string
    Where the first number in the array is always 0
    and the rest of the number in the array represents the length of matched prefix of the input string

    example:
        buildZList('abababab') => [0,0,6,0,4,0,2,0]
        the substring string from index 2 to end is: 'ababab'
        which is the prefix of the input string

        buildZList('abab' + '.' + 'ba') => [0, 0, 2, 0, 0, 0, 1]
        the number at index 2 is 2, which is the length of the needle, which means needle is in haystack

    Time Complexity: O(n)
    Space Complexity: O(n)
    :param s: str
    :return: List[int]
    """
    n = len(s)
    l, r = 0, 0
    z = [0] * n
    for i in range(1, n):
        if i > r:
            l, r = i, i
            while r < n and s[r - l] == s[r]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            if z[i - l] <= r - i:
                z[i] = z[i - l]
            else:
                l = i
                while r < n and s[r - l] == s[r]:
                    r += 1
                z[i] = r - l
                r -= 1

    return z


def buildKmpLpsList(s: str) -> List[int]:
    """
    The longest proper prefix which is also a suffix
    Used in KMP patter matching: buildZList(needle)

    Construct an array of length equal to the length of the input needle
    Where the first number in the array is always 0
    and the rest of the number in the array represents the length of array ending at current i that's also a prefix

    example:
        buildZList('AABAACAABAA') => [0,1,0,1,2,0,1,2,3,4,5]

    Time Complexity: O(n)
    Space Complexity: O(n)
    :param s: str
    :return: List[int]
    """
    n = len(s)
    lps = [0] * n
    pIndex, i = 0, 1
    while i < n:
        if s[i] == s[pIndex]:
            lps[i] = pIndex + 1
            pIndex, i = pIndex + 1, i + 1
        else:
            if pIndex == 0:
                lps[i] = 0
                i += 1
            else:
                pIndex = lps[pIndex - 1]
    return lps


def kmpSearch(needle: str, haystack: str) -> int:
    if needle == "":
        return 0

    m, n = len(haystack), len(needle)
    lps = buildKmpLpsList(needle)
    i, j = 0, 0
    while i < m:
        if haystack[i] == needle[j]:
            i, j = i + 1, j + 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]
        if j == n:
            return i - n
    return -1


def longestUniqueSubstring(s: str) -> int:
    indices = {}
    ans = 0
    l = 0
    for r, c in enumerate(s):
        if c not in indices or indices[c] < l:
            indices[c] = r
            ans = max(ans, r - l + 1)
        else:
            l = indices[c] + 1
            indices[c] = r

    return ans


if __name__ == "__main__":
    print(buildZList("abab" + "." + "ba"))
