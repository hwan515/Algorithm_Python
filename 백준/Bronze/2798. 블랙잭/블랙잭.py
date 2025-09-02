def blackjack(cards, target):
     max_sum = []
     for i in range(len(cards)):
         for j in range(i+1, len(cards)):
                for k in range(j+1, len(cards)):
                    total = cards[i] + cards[j] + cards[k]
                    if total <= target:
                        max_sum.append(total)
     return max(max_sum) if max_sum else 0

N, target = map(int, input().split())
cards = list(map(int, input().split()))
print(blackjack(cards, target))