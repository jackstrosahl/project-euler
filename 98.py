from collections import Counter

class HCounter(Counter):
    def __key(self):
        return tuple((k,self[k]) for k in sorted(self))
    def __hash__(self):
        return hash(self.__key())
    def __eq__(self, other):
        return self.__key() == other.__key()

letter_counts = {}
with open("p098_words.txt") as f:
    for word in f.read().replace('"','').lower().split(","):
        letter_count = HCounter(word)
        words = letter_counts.get(letter_count, None)
        if words is None:
            words = []
            letter_counts[letter_count] = words
        words.append(word)

no_anagrams = []
for letter_count, words in letter_counts.items():
    if len(words) == 1:
        no_anagrams.append(letter_count)

for no_anagram in no_anagrams:
    del letter_counts[no_anagram]

longest = 0
for letter_count, words in letter_counts.items():
    length = len(words[0])
    if length > longest:
        longest = length

number_counts = {}
i = 10
while True:
    square = i**2
    if square >= 10**longest:
        break
    number_count = HCounter(str(square))
    numbers = number_counts.get(number_count, None)
    if numbers is None:
        numbers = []
        number_counts[number_count] = numbers
    numbers.append(square)
    i += 1

no_anagrams = []
for number_count, numbers in number_counts.items():
    if len(numbers) == 1:
        no_anagrams.append(number_count)

for no_anagram in no_anagrams:
    del number_counts[no_anagram]

anagram_squares = set()
for number_count, numbers in number_counts.items():
    for number in numbers:
        anagram_squares.add(number)

def apply_subs(word, subs):
    num = ""
    for letter in word:
        num += subs[letter]
    return int(num)

highest = 0
out = ""
for letter_count, words in letter_counts.items():
    word = words[0]
    for number_count, numbers in number_counts.items():
        if len(str(numbers[0])) != len(word):
            continue
        for number in numbers:
            subs = {}
            used = set()
            number_str = str(number)
            for i, letter in enumerate(word):
                sub = subs.get(letter, None)
                digit = number_str[i]
                if sub is None and digit not in used:
                    subs[letter] = digit
                    used.add(digit)
                elif sub != digit:
                    subs = None
                    used = None
                    break
            if subs is not None:
                for onumber in numbers:
                    if number == onumber:
                        continue
                    for oword in words:
                        if word == oword:
                            continue
                        subbed = apply_subs(oword,subs)
                        if subbed == onumber:
                            best = max((number, onumber))
                            if best > highest:
                                highest = best
                                out = f"({number},{onumber}) ({word},{oword}) {subs}"

print(highest)
print(out)