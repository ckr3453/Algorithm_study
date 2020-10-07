def solution(participant, completion):
    
    participant.sort()
    completion.sort()
    
    for k, v in zip(participant, completion):
        if k != v:
            return k
        
    return participant[-1]