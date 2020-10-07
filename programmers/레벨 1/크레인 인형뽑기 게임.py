def solution(board, moves):
    answer_list = list()
    answer = 0
    for move in moves:
        # board index에 접근하기위해 1 감소
        move -= 1
        for i in range(len(board)):
            # 0이면 없는 칸이므로 다음칸 전진
            if board[i][move] == 0:
                continue
            else:
                answer_list.append(board[i][move])
                board[i][move] = 0
                break
    
    i = 0
    while i < len(answer_list) - 1:
        if answer_list[i] == answer_list[i+1]:
            del answer_list[i:i+2]
            answer += 2
            i = 0
        else:
            i += 1
    return answer