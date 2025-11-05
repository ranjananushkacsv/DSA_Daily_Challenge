def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for  word in strs:
            sorted_words = ' '.join(sorted(word))

            if sorted_words in anagram_map:
                anagram_map[sorted_words].append(word)

            else:
                anagram_map[sorted_words] = [word]

        return list (anagram_map.values())
'''
APPROACH - 

1. For anagrams we will sort every word
2. We are gonna use a dictionary (hashmap) where in the key :- will be sorted values and the values :- original values
3. we'll match both and return the final lsit of anagrams stored as anagram_maps.
'''