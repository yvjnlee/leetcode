class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)

        if n > m:
            return ""

        # learned about counter
        # https://www.geeksforgeeks.org/python-counter-objects-elements/
        ref, window = Counter(t), {}
        left, right = 0, 0
        # formed keeps track of how many characters we meet the req of
        formed = 0
        # rly smart way to keep track of sol in 1 line instead of 3
        res = float("inf"), None, None
        
        while right < m:
            # print(left, right, s[left:right+1])
            char = s[right]
            window[s[right]] = window.get(char, 0) + 1

            # checks to see if we meet the freq of the char in t
            if char in ref and window[char] == ref[char]:
                formed += 1

            # only enters once we meet or exceed the freq of all chars
            while left <= right and formed == len(ref):
                char = s[left]

                if right - left + 1 < res[0]:
                    # keep track of the match
                    res = (right - left + 1, left, right)
                    # print("MATCH", left, right, s[left:right+1])
                
                # make the window smaller to see if we can get a better solution
                window[char] -= 1
                if char in ref and window[char] < ref[char]:
                    formed -= 1
                
                left += 1
            right += 1
            # print(ref, window)

        length, left, right = res
        return "" if length == float("inf") else s[left:right+1]
