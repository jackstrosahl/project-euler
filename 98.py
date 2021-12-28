from collections import Counter

squares = []
i = 4
while True:
    square = i**2
    if square > 1e6:
        break
    squares.append(square)
    i += 1

letter_counts = {}
with open("p098_words.txt") as f:
    for word in f.read().replace('"','').lower().split(","):
        letter_counts[word] = Counter(word)  

anagrams_map = {}
def add_anagram(word,oword):
    anagrams = anagrams_map.get(word,None)
    if anagrams is None:
        anagrams = []
        anagrams_map[word] = anagrams
    anagrams.append(oword)

for word, letters in letter_counts.items():
    for oword, oletters in letter_counts.items():
        if word == oword or word == oword[::-1]:
            continue
        if letters == oletters:
            anagrams_map[word] = oword
            add_anagram(word,oword)


words = sorted(words,key=len,reverse=True)
print(words)
print(len(squares))