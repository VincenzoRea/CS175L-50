#average_from_input_file
#Vincenzo Rea 1326998
#CS175L
#Spring 2022

def main():
    f = open ('numbers.txt','r')
    total = 0.0
    number = 0.0
    line = ''

    for line in f:
        number = float(line)
        total += number

    f.close()

    print ('Total: ', total)


main()
