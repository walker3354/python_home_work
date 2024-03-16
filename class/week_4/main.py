def soultion(str_input):
    answer = dict()
    for i in str_input:
        if answer.get(i) is None:
            answer[i] = 1
        else:
            answer[i] += 1
    return answer


soultion('abbaaabb')
