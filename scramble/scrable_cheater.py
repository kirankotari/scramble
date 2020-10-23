import sys
import common

def valid_word(word, rack):
    avaliable_letter = rack[:]
    for letter in word:
        if letter not in avaliable_letter:
            return False
        avaliable_letter.remove(letter)
    return True

def compute_score(word):
    score = 0
    for letter in word:
        score = score + common.scores[letter.lower()]
    return score

if len(sys.argv) < 2:
    print('Usage: scramble.py [RACK]')
    exit(1)

rack = list(sys.argv[1].upper())
valid_words = {}

for word in common.wordlist:
    # print(f"{word} : {valid_word(word, rack)}")
    if valid_word(word, rack):
        score = compute_score(word)
        valid_words[word] = score

valid_words = {k: v for k, v in sorted(valid_words.items(), key=lambda item: item[1], reverse=True)}
for word, score in valid_words.items():
    print(f"{word} : {score}")