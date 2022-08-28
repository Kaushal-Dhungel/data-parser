import re

def data_parser():
    with open('data/data.txt', 'r') as file, open('output.csv', 'w') as out_file:
        lines = file.read().splitlines()
        half_list = []
        
        for line in lines:
            temp_line  = re.sub("\s{2,}", ",", line.strip())
            temp_line = temp_line.split(',')
            out_file.write(','.join([str(elem) for elem in temp_line[:3]]) + '\n')
            half_list.append(','.join([str(elem) for elem in temp_line[3:]]) + '\n')

        for line in half_list[1:]:
            out_file.write(line)

