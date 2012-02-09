def flatten(x):
    if type(x) == list:
        return [a for i in x for a in flatten(i)]
    else:
        return [x]
