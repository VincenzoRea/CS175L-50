#Vincenzo Rea 1326998
#CS175 L
#Spring 2022

import sys

def main():
    try:
        infile = open('numbers.txt', 'r')
    except IOError:
        print('There was an error trying to read the file.')
        sys.exit()

    sums_num = 0
    counter = 0

    for line in infile.readlines():
        counter += 1
        try:
            num = float(line)
        except ValueError:
            print('Non-numeric data found.')
            counter = counter - 1
            continue
        sums_num += num

        print(f'I read in {counter} number(s) Current number is: {num} Total is: {sums_num}')
        
main()
        
