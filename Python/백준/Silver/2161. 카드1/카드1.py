N = int(input())
cards = [i for i in range(1, N+1)]

bucket = []
while len(cards) > 1:
    bucket.append(cards.pop(0))
    cards.append(cards.pop(0))

bucket.extend(cards)
print(*bucket)