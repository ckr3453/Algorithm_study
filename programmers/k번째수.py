def solution(array, commands):
    answer = list()
    for i in range(len(commands)):
        temp = list()
        temp = array[commands[i][0]-1:commands[i][1]]
        temp.sort()
        answer.append(temp[commands[i][2]-1])
    return answer