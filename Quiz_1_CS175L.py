#Quiz 1 Lab
#Vincenzo Res
#CS175L
#Spring2022

years = int(input('Enter the number of years:'))
months = 12
sum = 0

if years < 1:
    print ('You have entered an invalid year.')
else:
    for year in range(years):
        print ('For year:',year + 1,)
        for month in range(months):
            print ('Enter the inches of rainfall for month',month + 1)
            rainfall = int(input('Enter the value of rainfall for the month:'))
            sum = sum + rainfall
    total_months = years * months
    average_rainfall = sum / total_months
print ('Total inches of rainfall:', sum)
print ('Number of months:',total_months)
print ('Average monthly rainfall:',average_rainfall)
            
            
        
    
