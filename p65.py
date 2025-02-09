# for item in ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93",
#              "-123.456e789", "46.e3"]:
#     if solution.isNumber(item):
#         print(f"Test case passed: {item}")
#     else:
#         print(f"Test case failed: {item}")
#
# for item in [".", "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53", "3.5e+3.5e+3.5"]:
#     if not solution.isNumber(item):
#         print(f"Test case passed: {item}")
#     else:
#         print(f"Test case failed: {item}")

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.lower()
        return self.isNumberHelper(True, True, True, False, False, s)

    def isNumberHelper(self, can_contain_sign: bool, can_be_decimal: bool, can_be_power: bool, can_be_empty: bool, can_start_with_e: bool,
                       s: str) -> bool:
        if s == '':
            return can_be_empty
        if s[0] == '+' or s[0] == '-':
            if not can_contain_sign:
                return False
            return self.isNumberHelper(False, can_be_decimal and True, can_be_power and True, False, False, s[1:])

        if s[0] == '.':
            if not can_be_decimal:
                return False
            return self.isNumberHelper(False, False, can_be_power and True, False, False, s[1:])

        if s[0] == 'e':
            if can_start_with_e:
                return self.isNumberHelper(True, False, False, False, False, s[1:])
            return False

        numeric_count = 0
        for i in range(len(s)):
            if s[i] == '.':
                if not can_be_decimal:
                    return False
                return self.isNumberHelper(False, False, True, True, True, s[i + 1:])
            if s[i] == 'e':
                if not can_be_power:
                    return False
                return self.isNumberHelper(True, False, False, False, False, s[i + 1:])
            if not s[i].isnumeric():
                return False

            numeric_count += 1
        return True
