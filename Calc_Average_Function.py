#Calculate Average and Grade with Functions
#Vincenzo Rea
#CS175L
#Spring2022

#num = score
score1 = 0
score2 = 0
score3 = 0
score4 = 0
score5 = 0

def main():
    First_Question = input('Would you like to average test scores? Yes or No?')
    while First_Question == 'Yes':
        score1 = float(input('Enter score 1:'))
        score2 = float(input('Enter score 2:'))
        score3 = float(input('Enter score 3:'))
        score4 = float(input('Enter score 4:'))
        score5 = float(input('Enter score 5:'))
        letter1 = determine_grade(score1)
        letter2 = determine_grade(score2)
        letter3 = determine_grade(score3)
        letter4 = determine_grade(score4)
        letter5 = determine_grade(score5)
        score_average = calc_average(score1, score2, score3, score4, score5)
        letterA = determine_grade(score_average)
        print ('Score\tNumeric Grade  Letter Grade')
        print ('-------------------------------------')
        print (f'score 1:  {score1}\t\t{letter1}')
        print (f'score 2:  {score2}\t\t{letter2}')
        print (f'score 3:  {score3}\t\t{letter3}')
        print (f'score 4:  {score4}\t\t{letter4}')
        print (f'score 5:  {score5}\t\t{letter5}')
        print (f'Average:  {score_average}\t\t{letterA}')
        First_Question = repeat()
        
        






    print ('There are no test scores to be tested.')
    
    
    
    
    
    



def determine_grade(score):
        if 60 >= score:
            letter_grade = 'F'
        elif 60 <= score <= 69:
            letter_grade = 'D'
        elif 70 < score <= 79:
            letter_grade = 'C'
        elif 80 < score <= 89:
            letter_grade = 'B'
        else:
            letter_grade = 'A'
        return letter_grade

    
        
        
    







def calc_average(score1, score2, score3, score4, score5):
    test_total = (score1 + score2 + score3 + score4 + score5)
    test_average = test_total / 5
    return test_average
    
def repeat():
    repeatQ = input('Would you like to do another calculation:')
    return repeatQ
    

main()


    

