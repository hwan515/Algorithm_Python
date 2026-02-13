def solution(participant, completion):
    counts = {}
    for person in participant:
        counts[person] = counts.get(person, 0) + 1
    
    for person in completion:
        counts[person] -= 1
    
    for person, cnt in counts.items():
        if cnt == 1:
            return person