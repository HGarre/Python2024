#READ ME
#filter_lines function

#Description
#Filter_lines is a function that checks each line of a file for the presents or absenc
# of a given regular expression patter and prints all coresponding lines to a new file

#Parameters
#input_file: A string giving the name of a file that should be checked for the presence or absence of the pattern
#output_file: A string giving the name of a file of which the lines that give a hit should be printed
#pattern: A string that uses the regular expression syntax to describe the pattern to search for
# contain: A boolean to choose whether presence (True) or absence (False) of the pattern should be checked

#Limitations
#If the pattern does not use valid regular expression syntax, a empty file is returned
#If the pattern is not found an empty file is returned without warning

#Structures
# A for-loop is used to read the input_file line by line
# A if-statement is used to check whether the absence or presence of the pattern should be checked
# A if-statement is used check whether the pattern is present/absent in the line and print those lines t a output_file

#Output
#The function does not return any output but created a file with all lines that contain/not contain the pattern



def filter_lines (input_file, output_file, pattern, contain):
    import re
    input = open(input_file, 'r')
    output = open(output_file, 'w')
    s = re.compile(pattern)
    for line in input:
        if contain:
            if s.search(line):
                output.write(line)
        else:
            if not s.search(line):
                output.write(line)
    input.close()
    output.close()

filter_lines('filter_test_data.txt', 'filter_test_output.txt', 'Latitute|Longitute', True)