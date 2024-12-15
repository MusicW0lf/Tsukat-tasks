from collections import defaultdict
def group_anagrams(words):
    
    anagram_map = defaultdict(list)

    for word in words:
        char_count = [0] * 26
        for char in word:
            char_count[ord(char) - ord('a')] += 1
        anagram_map[tuple(char_count)].append(word)

    return list(anagram_map.values())

def test_group_anagrams_positive():
    # setup
    anagrams = {
        0: ["eat","tea","tan","ate","nat","bat"],
        1: [""],
        2: ["a"]}
    expecteds = {
        0: [["bat"],["nat","tan"],["ate","eat","tea"]],
        1: [[""]],
        2: ["a"]}
    
    #tests
    for i in range(3):
        result = {frozenset(group) for group in group_anagrams(anagrams[i])}
        expected =  {frozenset(group) for group in expecteds[i]}
        assert result == expected, f"\nError in {i}th test:\nExpected: {sorted(expected)}\nGot: {sorted(result)}"
        print(f"{i}th test passed")

test_group_anagrams_positive()