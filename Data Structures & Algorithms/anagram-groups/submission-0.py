class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            letter_store = [0] * 26
            for c in word:
                letter_store[ord(c) - ord('a')] += 1
            result[tuple(letter_store)].append(word)



        return list(result.values())
                        

            