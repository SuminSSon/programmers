# 자릿수 더하기

def solution(n):
    n = str(n)
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    return sum
