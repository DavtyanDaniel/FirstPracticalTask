import csv

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

RA_DEC = input('Please input equtorial cordinates(RA DEC)')
RA_DEC_TUPLE = tuple(my_split(RA_DEC))
FOV_H_V = input("Please enter HFOV and VFOV")
FOV_H_V_TUPLE = tuple(my_split(FOV_H_V))
NUMBER_OF_STARS = int(input("Please enter the number of stars"))

with open("337.all.tsv", 'r') as tsv_file:

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

filtered_stars = []
# going through ra/dec coordinates
for i in data:
    if (square_w_l <= float(i[0]) <= square_w_r) and (square_h_l <= float(i[1]) <= square_h_r):
        filtered_stars.append(i)

for i in filtered_stars:
    print(i)
