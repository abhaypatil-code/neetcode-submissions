class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_map = defaultdict(list)

        for word in strs:
            # Key = sorted version of the word
            key = ''.join(sorted(word))
            anagram_map[key].append(word)

        return list(anagram_map.values())



        