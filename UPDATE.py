file_numbers = list()
with open("readme.md") as f:
    lines = f.readlines()

    for i in range(6, len(lines)):
        line = lines[i].split('|')[-2]
        file_name = line.split('/')[-1]
        number = file_name.split('.')[0]

        file_numbers.append(int(number))

import os

pyfiles = os.listdir(os.curdir)

for pf in pyfiles:
    if '.py' in pf and not 'UPDATE' in pf:
        number = int(pf.split('.')[0])

        if number not in file_numbers:
            print(number)