text = input("Text: ")
words = text.split()

word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

max_word_length = max(len(word) for word in word_counts)

sorted_words = sorted(word_counts.keys())

for word in sorted_words:
    print(f"{word:{max_word_length}} : {word_counts[word]}")