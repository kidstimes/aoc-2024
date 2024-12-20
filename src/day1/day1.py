import os


def read_numbers(filename):
    first_list = []
    second_list = []
    script_dir = os.path.dirname(__file__)
    filename = os.path.join(script_dir, filename)
    with open (filename, "r") as file:
        for line in file:
            numbers = line.split() 
            first_list.append(int(numbers[0]))
            second_list.append(int(numbers[1]))
    return first_list, second_list


def sum_sorted_number_diff(lst1, lst2):
    difference = 0
    lst1 = sorted(lst1)
    lst2 = sorted(lst2)
    for i in range(len(lst1)):
        difference += abs(lst1[i] - lst2[i])
    print("The sum of distances between two sorted assay is "+ str(difference)) 
  

def find_similarity(lst1, lst2):
    sum=0
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                sum += lst1[i]
    print("The similarity is " + str(sum))


print("real problem")
lst1, lst2= read_numbers("day1.txt")
sum_sorted_number_diff(lst1, lst2)
find_similarity(lst1, lst2)


