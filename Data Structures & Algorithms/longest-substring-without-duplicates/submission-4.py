class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #convert str to set
        #count -> repeat? -> HAS to be in order next to eachotehr
        #seen 
        #SLIDING window prob...like i though...
        #something minus front index of list
        if len(set(s)) == 1:
            return 1
        curr_longest = 0
        seen = set()
        window = 0
        for i, val in enumerate(s):
            while val in seen:
                seen.remove(s[window])
                window += 1
            seen.add(val)
            if (i-window+1) > curr_longest:
                    curr_longest = i-window+1
            
        return curr_longest
            
        # abcabcbb
        #zxy xyz

        #something points at first index and last and see if contian dup


