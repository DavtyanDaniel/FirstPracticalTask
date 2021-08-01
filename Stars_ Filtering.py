import csv
import math
from datetime import datetime


def my_split(string, delimiters= ' '):
    result = []
    word = ''
    for c in string:
        if c not in delimiters:
            word += c
        elif word:
            result.append(word)
            word = ''

    if word:
        result.append(word)
    return result


# it is a bubble sort (sorting by last element of list)
def my_sort(sub_list):
    list1 = len(sub_list)
    for i in range(0, list1):
        for j in range(0, list1-i-1):
            if sub_list[j][-1] > sub_list[j + 1][-1]:
                tempo = sub_list[j]
                sub_list[j] = sub_list[j + 1]
                sub_list[j + 1] = tempo
    return sub_list


RA_DEC = input('Please input equtorial cordinates(RA DEC)')
RA_DEC_TUPLE = tuple(my_split(RA_DEC))
FOV_H_V = input("Please enter HFOV and VFOV")
FOV_H_V_TUPLE = tuple(my_split(FOV_H_V))
NUMBER_OF_STARS = int(input("Please enter the number of stars"))
filtered_stars = []
result = []

with open("cleaned_stars.tsv", 'r') as tsv_file:

    next(tsv_file)
    # get number of columns
    for line in tsv_file.readlines():
        array = my_split(line, delimiters=',')

    num_of_columns = len(array)

    tsv_file.seek(0)
    next(tsv_file)

    reader = csv.reader(tsv_file, delimiter='\t')
    included_cols = [5, 6, 7, 22]
    data = []
    for row in reader:
        content = list(row[i] for i in included_cols)
        data.append(content)


data.pop(0)
# square's weight left number
square_w_l = float(RA_DEC_TUPLE[0]) - (float(FOV_H_V_TUPLE[0])/2)
# square's weight right number
square_w_r = float(RA_DEC_TUPLE[0]) + (float(FOV_H_V_TUPLE[0])/2)
# square's height left number
square_h_l = float(RA_DEC_TUPLE[1]) - (float(FOV_H_V_TUPLE[1])/2)
# square's height right number
square_h_r = float(RA_DEC_TUPLE[1]) + (float(FOV_H_V_TUPLE[1])/2)


# going through ra/dec coordinates and filtering them
for i in data:
    if (square_w_l <= float(i[0]) <= square_w_r) and (square_h_l <= float(i[1]) <= square_h_r):
        filtered_stars.append(i)

my_sort(filtered_stars)
i = 0

# checking if given number of stars bigger than filtered stars
if len(filtered_stars) < NUMBER_OF_STARS:
    NUMBER_OF_STARS = len(filtered_stars)

# distance calculation
while i < NUMBER_OF_STARS:
    result.append(filtered_stars[i])

    distance = math.sqrt(pow(float(filtered_stars[i][0]) - float(RA_DEC_TUPLE[0]), 2) + \
                               pow(float(filtered_stars[i][1]) - float(RA_DEC_TUPLE[1]), 2))
    result[i].append(distance)
    i = i + 1

# sorting by distance
my_sort(result)

for i in filtered_stars:
    print(i)

# creating and writing new csv file
header = ['RA', 'DEC', 'ID', 'Magnitude', 'Dis_from_gv_point']

# Creating variable with a current time
file_name = datetime.now().strftime("%d%m%Y-%H%M%S")


with open(file_name, 'w') as f:
    writer = csv.writer(f)
    # Writing the header(column names)
    writer.writerow(header)
    # Writing results in csv file
    writer.writerows(result)



