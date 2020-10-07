def solution(answers):
    answer = []
    # 1번 : 1,2,3,4,5 반복
    # 2번 : 2,1, 2,3, 2,4, 2,5 반복
    # 3번 : 3,3, 1,1, 2,2, 4,4, 5,5 반복
    people = {'1' : [1,2,3,4,5], '2' : [2,1,2,3,2,4,2,5], '3' : [3,3,1,1,2,2,4,4,5,5] }
    for i in people:
        success_percent = 0
        limit1 = int(len(answers) / len(people[i])) + 1
        people[i] *= limit1
        for j in range(len(answers)):
            if answers[j] == people[i][j]:
                success_percent += 1
                
        people[i] = success_percent
    
    people = sorted(people.items(), key=lambda x : x[1], reverse=True)
    answer.append(int(people[0][0]))
    for i in range(1, len(people)):
        if people[i][1] == people[0][1]:
            answer.append(int(people[i][0]))
    answer.sort()
    return answer