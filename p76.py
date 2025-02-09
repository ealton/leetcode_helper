class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = {}
        s_dict = {}

        def isTsetValid() -> bool:
            for k, v in t_dict.items():
                if s_dict[k] < v:
                    return False
            return True

        for item in t:
            if item in t_dict:
                t_dict[item] += 1
            else:
                t_dict[item] = 1
            if item not in s_dict:
                s_dict[item] = 0

        # print(t_dict)
        # print(s_dict)
        s_index = 0
        e_index = 0
        s_size = len(s)
        min_size = s_size + 1
        result = ''

        while e_index < s_size:
            # print(f"OutLoop: {e_index}")
            while not isTsetValid() and e_index < s_size:
                if s[e_index] in s_dict:
                    s_dict[s[e_index]] += 1
                e_index += 1

            # print(f"Found eIndex: {e_index}")
            if not isTsetValid():
                # print(f"tSetNotValid: {s_dict}, {t_dict}")
                break

            while isTsetValid():
                if s[s_index] in s_dict:
                    s_dict[s[s_index]] -= 1
                s_index += 1
            if e_index - (s_index - 1) < min_size:
                min_size = e_index - (s_index - 1)
                result = s[s_index-1:e_index]
        if min_size > len(s):
            return ""
        return result


