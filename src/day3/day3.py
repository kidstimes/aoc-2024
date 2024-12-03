import os
import re


def read_txt_to_string(filename):
    script = os.path.dirname(__file__)
    filename = os.path.join(script, filename)
    with open(filename, 'r') as file:
        string = file.read()
    return string


def calculate_result(string):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, string)
    sum = 0
    for eachpair in matches:
        sum += int(eachpair[0])*int(eachpair[1])
    print (sum)
    
    
def calculate_result_part2(string):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    sum = 0 
    sublists = string.split('do()')
    for each in sublists:
        new_sublist=each.split('don\'t')
        matches = re.findall(pattern, new_sublist[0])
        for eachpair in matches:
            sum += int(eachpair[0])*int(eachpair[1])
    print (sum)

    

string = read_txt_to_string('day3.txt')
calculate_result(string)
calculate_result_part2(string)
