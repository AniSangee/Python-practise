# Function to manually sort a word (using Bubble Sort)
def manual_sort(word):
    word = list(word)  # Convert string to list
    n = len(word)
    for i in range(n):
        for j in range(n - i - 1):
            if word[j] > word[j + 1]:  # Swap if out of order
                word[j], word[j + 1] = word[j + 1], word[j]
    return ''.join(word)  # Convert list back to string

# Function to group anagrams
def group_anagrams(words):
    groups = []  # To store anagram groups
    for word in words:
        sorted_word = manual_sort(word)  # Sort word manually
        found = False
        for group in groups:
            if manual_sort(group[0]) == sorted_word:  # Compare manually sorted versions
                group.append(word)
                found = True
                break
        if not found:
            groups.append([word])  # Create a new group
    return groups

# Input list
N = ['act', 'atc', 'cta', 'god', 'dog']

# Get grouped anagrams
M = group_anagrams(N)

# Print result
print(M)
