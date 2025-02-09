class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        def helper(s: str, t: str, s_index: int) -> int:
            if (t, s_index) in cache:
                return cache[(t, s_index)]
            if len(t) == 1:
                num = 0
                for i in range(s_index, len(s)):
                    if s[i] == t: num += 1
                cache[(t, s_index)] = num
                return num
            num = 0
            for i in range(s_index, len(s)-len(t) + 1):
                if s[i] == t[0]:
                    new_num = helper(s, t[1:], i+1)
                    # print(f'helper ({t[1:]}, {i+1}) = {new_num}')
                    num += new_num
            cache[(t, s_index)] = num
            return num
        print(cache)
        return helper(s, t, 0)
