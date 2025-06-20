# 1181
N = int(input())

words = set()

for _ in range(N):
    words.add(input().strip())
words_list = list(words)

words_list.sort(key=lambda word: (len(word), word))

for word in words_list:
    print(word)