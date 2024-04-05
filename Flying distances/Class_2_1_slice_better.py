def slice_better(str):
    word = ''
    out = []
    for letter in str:
        if letter != ' ':
            word += letter
        else:
            if word != '': #test needed to not add '' to list
                out += [word]
            word = ''
    if word != '': #another test in case the last letter is a space
        out += [word]
    return out

print(slice_better('split this string in words'))
print(slice_better(' split this     string in words    '))