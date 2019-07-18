def spy_game(arr):
    arr=[str(x) for x in arr]
    result = ''
    for el in arr:
        if el == '0':
            result+=el
        if el == '7':
            result += el
            break
    return result == '007'
print(spy_game([1,7,2,0,4,5,0]))
