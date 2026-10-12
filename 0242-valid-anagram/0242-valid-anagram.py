class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # sort_s = sorted(s)
        # sort_t = sorted(t)
        # if sort_s == sort_t:
        #     return True
        # else:
        #     return False

        if len(s) != len(t):
            return False
        ch_map = {}
        for ch in s:
            ch_map[ch] = ch_map.get(ch, 0) + 1
        for ch in t:
            if ch not in ch_map:
                return False
            else:
                if ch_map[ch] == 0:
                    return False
                else:
                    ch_map[ch] -= 1
        return True