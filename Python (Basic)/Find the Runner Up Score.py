if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    runners = list(arr)
    first_place = float('-inf')
    second_place = float('-inf')
    
    for runner in runners:
        if runner > first_place:
            second_place = first_place
            first_place = runner
        elif runner > second_place and runner != first_place:
            second_place = runner
    print(second_place)
