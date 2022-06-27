def print_without_repeatition(*args):
    pass
    anwser = set(*args)
    return list(anwser)

print(print_without_repeatition([1,3,4,2,1,5,6,5,8]))