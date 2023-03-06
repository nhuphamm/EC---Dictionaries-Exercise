filename = 'book of John text.txt'

words_to_count = ['Father', 'God', 'Christ', 'Spirit', 'life', 'man']

word_counts = {word: 0 for word in words_to_count}

with open(filename) as f:
    for line in f:
        for word in line.split():

            if word.lower() in word_counts:
                word_counts[word.lower()] += 1
            elif word in word_counts:
                word_counts[word] += 1
            # elif word == "Spirit":
            #     word_counts[word] += 1

for word, count in word_counts.items():
    print(f"{word}: {count}")
