def solution(array, commands):
    return [sorted(array[commands[i][0]-1 : commands[i][1]])[commands[i][2]-1] for i in range(len(commands))]