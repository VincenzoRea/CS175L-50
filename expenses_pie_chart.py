#EXpense Pie Chart
#Vincenzo Rea
#CS 175L
#Spring 2022

import matplotlib.pyplot as plt

def main():
    expenses_file = open("expenses.txt","r")
    categories = []
    amounts = []
    for line in expenses_file:
        line_list = line.split("\t")
        categories.append(line_list[0])
        amounts.append(line_list[1])
    expenses_file.close()
   
    plt.pie(amounts, labels=categories)
    plt.title('Expenses Last Month')
    plt.show()

if __name__ == '__main__':
    main()
