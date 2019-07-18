def multiply(numbers):
    res = 1
    for n in numbers:
        res*=n
    return res
print(multiply([1,2,3,-4]))
