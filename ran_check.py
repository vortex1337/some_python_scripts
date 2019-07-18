def ran_check(num,low,high):
    if num>low and num<high:
        return '{} is between {} and {}'.format(num, low, high)
    else:
        return '{} is not in the range {}:{}'.format(num, low, high)
print(ran_check(5,2,7))
def ran_bool(num,low,high):
    return num>low and num<high
print(ran_bool(5,2,7))
