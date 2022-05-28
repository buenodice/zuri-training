# check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagrams(m1, m2):
    if (sorted(m1) == sorted(m2)):
        print(sorted(m1), sorted(m2))
        return True
        Else
        return false

print(find_anagrams("below", "elbow"))