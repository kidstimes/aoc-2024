import os


def read_input_to_list(filename):
    script = os.path.dirname(__file__)
    filename = os.path.join(script, filename)
    reports = []    
    with open(filename, "r") as file:
        for line in file:
            numbers = line.split()
            report = [int(i) for i in numbers]
            reports.append(report)
    return reports


def check_safe_ascending(lst):
    is_safe = True
    for i in range(len(lst)-1):
        if lst[i+1]-lst[i] > 3 or lst[i+1]-lst[i]<1:
            is_safe = False
            break
    return is_safe
            

def check_safe_descending(lst):
    is_safe = True
    for i in range(len(lst)-1):
        if lst[i]-lst[i+1] > 3 or lst[i]-lst[i+1] < 1:
            is_safe = False
            break
    return is_safe
    

def calculate_safe_reports(reports):
    num_safe = 0
    for report in reports:
        if check_safe_ascending(report) or check_safe_descending(report):
            num_safe += 1
    print('The number of safe reporst is '+ str(num_safe)) 


def check_safe_dampener(report):
    is_safe_dampener = False
    for i in range(len(report)):
        new_report = report[:i]+report[i+1:]
        if check_safe_ascending(new_report) or check_safe_descending(new_report):
            is_safe_dampener = True
    return is_safe_dampener
            

def calculate_safe_reports_with_dampener(reports):
    num_safe = 0
    for report in reports:
        if check_safe_ascending(report) or check_safe_descending(report) or check_safe_dampener(report):
            num_safe += 1
    print('The number of safe reporst with dampener is '+ str(num_safe)) 


reports=read_input_to_list('day2.txt')
calculate_safe_reports(reports)
calculate_safe_reports_with_dampener(reports)