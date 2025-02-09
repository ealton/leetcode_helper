class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = {}
        for item in t:
            if item in m:
                m[item] += 1
            else:
                m[item] = 1

        print(m)

        start = 0
        end = 0
        counter = len(t)
        min_start = 0
        min_length = len(s) + 1
        size = len(s)

        while end < size:
            if s[end] in m and m[s[end]] > 0:
                counter -= 1

            if s[end] in m:
                m[s[end]] -= 1
            end += 1

            print(f"counter, end = {counter} {end}")

            while counter == 0:
                print("counter is zero")
                if end - start < min_length:
                    min_start = start
                    min_length = end - start

                if s[start] in m:
                    m[s[start]] += 1
                    if m[s[start]] > 0:
                        counter += 1
                start += 1

        if min_length > len(s):
            return ""
        return s[min_start: min_start + min_length]


