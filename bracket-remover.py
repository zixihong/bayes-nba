def remove_bracket(brackets):
    for bracket in brackets:
        if bracket == '[' or bracket == ']':
            brackets = brackets.replace(bracket, '')
    return brackets

x = '[[120, 237, 86, 237], [182, 364, 141, 396], [83, 169, 39, 105], [154, 265, 37, 114], [53, 84, 19, 51], [7, 14, 6, 21], [22, 46, 1, 1], [79, 151, 0, 1]]'
print(remove_bracket(x))