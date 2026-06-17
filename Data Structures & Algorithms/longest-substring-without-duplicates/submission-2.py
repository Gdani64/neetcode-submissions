from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1

        max_unique_length = 0
        q = deque()
        unique_char_map = {}
        for i,c in enumerate(s):
            print(unique_char_map)
            
            if c in unique_char_map:
                while q[0] != c:
                    unique_char_map.pop(q.popleft())
                unique_char_map.pop(q.popleft())
            
            unique_char_map[c] = i
            q.append(c)

            max_unique_length = max(max_unique_length, len(unique_char_map))
            print(unique_char_map)
            print(max_unique_length)
            print("\n")
        
        return max_unique_length