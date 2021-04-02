from collections import Counter
text = 'lorem ipsum dolor sit amet amet amet'
words = text.split(' ')
counter = Counter(words)
most_common, occurrences = counter.most_common()[0]
longest = max(words, key=len)
print(f"Occurs most often: {most_common},\nThe longest: {longest}")
