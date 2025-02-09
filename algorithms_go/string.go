package algorithmsgo

// Used in pattern matching: buildZList(needle + "." + haystack)
// and check for length(needle) in result
// Construct an array of length equal to the length of the input string
// where the first number is always 0, and the reset of the number
// each represents the length of matched prefix
// of the input string
//
// example:
//
//	buildZList('abababab') => [0,0,6,0,4,0,2,0]
//	the substring string from index 2 to end is: 'ababab'
//	which is the prefix of the input string
//
//	buildZList('ba' + '.' + 'abab') => [0, 0, 2, 0, 0, 0, 1]
//	the number at index 2 is 2, which is the length of the needle,
//  which means needle is in haystack

// Time Complexity: O(n)
// Space Complexity: O(n)
func BuildZList(s string) []int {
	l, r, n := 0, 0, len(s)
	z := make([]int, n)

	// Starting from index 1 because index 0 doesn't matter
	for i := 1; i < n; i++ {
		if i > r {
			l, r = i, i
			for r < n && s[r-l] == s[r] {
				r++
			}
			z[i] = r - l
			r -= 1
		} else {
			if z[i-l] <= r-i {
				z[i] = z[i-l]
			} else {
				l = i
				for r < n && s[r-l] == s[r] {
					r++
				}
				z[i] = r - l
				r -= 1
			}
		}
	}
	return z
}

func BuildKmpLpsList(s string) []int {
	n := len(s)
	lps := make([]int, n)
	pIndex, i := 0, 1
	for i < n {
		if s[i] == s[pIndex] {
			lps[i] = pIndex + 1
			pIndex, i = pIndex+1, i+1
		} else {
			if pIndex == 0 {
				lps[i] = 0
				i += 1
			} else {
				pIndex = lps[pIndex-1]
			}
		}
	}
	return lps
}

// Kmp algorithm to perform string search
func KmpSearch(needle string, haystack string) int {
	if needle == "" {
		return 0
	}

	m, n := len(haystack), len(needle)
	lps := BuildKmpLpsList(needle)
	i, j := 0, 0
	for i < m {
		if haystack[i] == needle[j] {
			i, j = i+1, j+1
		} else {
			if j == 0 {
				i += 1
			} else {
				j = lps[j-1]
			}
		}
		if j == n {
			return i - n
		}
	}
	return -1
}

func LongestUniqueSubstring(s string) int {
	indices := map[rune]int{}
	ans, l := 0, 0
	for r, c := range s {
		cIndex, exists := indices[c]
		if !exists || cIndex < l {
			indices[c] = r
			ans = max(ans, r-l+1)
		} else {
			l = cIndex + 1
			indices[c] = r
		}
	}
	return ans
}
