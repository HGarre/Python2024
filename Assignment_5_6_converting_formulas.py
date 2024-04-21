'''
Converting formulas
In this assignment, we are building a function that converts an expression with parentheses into a
series of expressions without parentheses.
Write a regular expression that recognizes a sub-string, that is enclosed in a pair of parentheses, and
that does not contain parentheses inside the sub-string. Check this regular expression using the
Find/Replace functionality of PyCharm in an editor window.
Use this regular expression, or a slightly adapted version of it, to replace the sub-string and its
parentheses by another string. Check this regular expression using the Find/Replace functionality of
PyVharm in an editor window.
Make a RegexObject for the regular expression, and use it to retrieve the sub-string between the
parentheses, and also to replace the sub-string by another string. Use method group of the
MatchObject returned from the search.
By applying the preceding step to a string that contains parentheses, convert it into a pair of strings.
The first string represents an assignment statement that defines a variable for the enclosed substring. The second string represents the original expression with the new variable substituted for the
enclosed sub-string along with its parentheses. For example:
'y*(4-x)*(2+a)' is
converted into the pair:
'qb = 4-x'
'y*qb*(2+a)'
We can replace any number of parentheses by means of this kind of substitutions, working from the
inside out. When starting with a list that contains only the input string, replacing each string that has
parentheses into a pair, ultimately one ends up with a list of strings without parentheses.
Complete the exercise by writing a function that converts an expression with parentheses into an
equivalent series of expressions without parentheses.
For example, the string
'a+(3-x)/(y*(4-x)*(2+a))'
should be converted into a list like this:
[ 'qa = 3-x',
'qb = 4-x',
'qc = 2+a',
'qd = y*qb*qc',
'a+qa/qd' ]
by a series of substitutions:
'a+(3-x)/(y*(4-x)*(2+a))'
'a+qa/(y*(4-x)*(2+a))'
'a+qa/(y*qb*(2+a))'Assignments Programming in Python 9 INF – 2021-10-27
'a+qa/(y*qb*qc)'
'a+qa/qd'
The function is free to choose names for the variables.
[Hint: let all new variables start with a letter that does not occur in the given string.]
'''

import re

def take_apart_formula(formula):
    pattern = '\([^()]+\)'
    variables = 'pqrstovw'
    indices = 'abcdefghijklmn'
    i = 0
    set = False
    while i < len(variables) and set == False:
        if indices[i] in formula:
            var = variables[i]
            set = True
        else:
            i += 1
    if not set:
        var = 'group'
    m = re.search(pattern, formula)
    list = []
    ind = 0
    while m != None:
        found = m.group()
        substitution = var + indices[ind] + ' = ' + found[1:-1]
        list += [substitution]
        formula = formula[:m.start()] + var+indices[ind] + formula[m.end():]
        m = re.search(pattern, formula)
        ind += 1
    list += [formula]
    return list

string = 'a+(3-q)/(y*(4-x)*(2+a))'

print(take_apart_formula(string))
# output: ['pa = 3-q', 'pb = 4-x', 'pc = 2+a', 'pd = y*pb*pc', 'a+pa/pd']