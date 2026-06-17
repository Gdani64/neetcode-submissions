class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1

        most_frequent_char = 'A'
        most_frequent_val = 0
        max_len = 0
        l = 0
        str_map = {
    "A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0,
    "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0,
    "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0
}
        
        def get_window_size()->int:
            size = r - l + 1
            print('window_size='+str(size))
            return size

        def is_valid_window(most_frequent_char_count)->bool:
            print('most_frequent_char_count='+str(most_frequent_char_count))
            res = get_window_size() - most_frequent_char_count <= k
            print('is_valid_window='+str(res))
            return res

        for r in range(len(s)):
            most_frequent_val = 0
            nb_unique_chars = 0
            str_map[s[r]] += 1
            print(str_map)
            for char, count in str_map.items():
                if count > 0:
                    nb_unique_chars += 1
                if count > most_frequent_val:
                    most_frequent_char = char
                    most_frequent_val = count
            
            if is_valid_window(most_frequent_val):
                max_len = max(max_len, get_window_size())
            else:
                str_map[s[l]] -= 1
                l += 1
                
            print("l={0};r={1}".format(l,r))
            print("\n")

        
        return max_len
