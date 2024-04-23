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
    pattern = '\([^()]+\)' #matches one or more (+) characters that are not (^) brackets (\ to escape the special character) between brackets
    variables = 'pqrstovw' #possible main names for the variables that are created
    indices = 'abcdefghijklmn' #indices for the variables to be created (limitation: doubles if more than 14 terms in brackets need to be substituted)
    i = 0
    set = False
    while i < len(variables)-1 and set == False: #loop through all possible variable names until a decition is made (set = true)
        if variables[i] not in formula: # if the current variable name is not used in the formula, pick it and stop the loop
            var = variables[i]
            set = True
        else: # else try the next possible variable name
            i += 1
    if not set: # if (very improbale but possible) all variables 'pqrstovw' are used in the formula, groupa, groupb, etc is used instead
        var = 'group'
    m = re.search(pattern, formula) #find innermost expression
    list = []
    ind = 0
    while m != None:
        found = m.group() #extract the expression
        substitution = var + indices[ind] + ' = ' + found[1:-1] #construct a string that states the new variable equal to this expression (without the flanking brackets)
        list += [substitution] #add it to the list
        formula = formula[:m.start()] + var+indices[ind] + formula[m.end():] #update the formula with the new variable between the start and end of the expression
        m = re.search(pattern, formula) #find the new innermost expression
        ind += 1
    list += [formula] #add the remaining formula to the list
    return list

string = 'a+(3-p)/(y*(4-x)*(2+a))'

print(take_apart_formula(string))
# output: ['pa = 3-q', 'pb = 4-x', 'pc = 2+a', 'pd = y*pb*pc', 'a+pa/pd']