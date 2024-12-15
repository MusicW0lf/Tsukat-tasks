import random
import string
import time
import matplotlib.pyplot as plt
from collections import defaultdict
def group_anagrams(words):
    start_time = time.time()

    anagram_map = defaultdict(list)

    for word in words:
        char_count = [0] * 26
        for char in word:
            char_count[ord(char) - ord('a')] += 1
        anagram_map[tuple(char_count)].append(word)

    result = list(anagram_map.values())

    return time.time() - start_time

def generate_anagram_strs(size: int, length: int) -> list[str]:
    return [''.join(random.choices(string.ascii_lowercase, k=length)) for _ in range(size)]

def measure_execution_time(size_values, lengths):
    execution_times = {length: [] for length in lengths}

    for length in lengths:
        for size in size_values:
            anagrams = generate_anagram_strs(size, length)
            execution_times[length].append(group_anagrams(anagrams))

    return execution_times

size_values = [100, 200, 500, 1000, 2000, 5000, 10000]
lengths = [3, 5, 10, 100, 1000, 2000, 5000]
execution_times = measure_execution_time(size_values, lengths)

for length in lengths:
    plt.plot(size_values, execution_times[length], marker='o', label=f'Length {length}')
plt.title('Execution Time vs Number of Anagrams')
plt.xlabel('Number of Anagrams')
plt.ylabel('Execution Time (Seconds)')
plt.grid(True)
plt.legend()
plt.show()

# time complexity O(n*m)