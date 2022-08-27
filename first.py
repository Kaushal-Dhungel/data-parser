import re

with open('data.txt', 'r') as file, open('output.csv', 'w') as out_file:
    lines = file.read().splitlines()
    for line in lines:
        temp_line  = re.sub("\s{2,}", ",", line.strip()) + '\n'
        # temp_line = temp_line + '\n'
        out_file.write(temp_line)
