#CS175
#VincenzoRea
#Restaurant_sequence with loop (v2)
vegan = 'no'
vegetarian = 'no'
gluten_free= 'no'


Search = input('Would you like to make a search? (Yes or No)')
if Search == 'No':
    print ('There are no more searches to be made')





while Search != 'No':
    vegetarian = input('Is anyone in your party a vegetarian?')

    if vegetarian == 'yes' or vegetarian == 'no':
        vegan = input('Is anyone in your party vegan?')

    if vegan == 'yes' or vegan == 'no':
        gluten_free = input ('Is anyone in your party gluten free?')

    print ('Here are your restaurant choices:')

    if gluten_free == 'yes' and vegan == 'yes' and vegetarian == 'yes':
        print ('Corner Cafe')
        print ("The Chef's Kithcen")

    if gluten_free == 'no' and vegan == 'no' and vegetarian == 'no':
        print ('Corner Cafe')
        print ("The Chef's Kithcen")
        print ("Joe's Gormet Burgers")
        print ('Main Street Pizza Company')
        print ("Mama's Fine Italian")

    if gluten_free == 'yes' and vegan == 'no' and vegetarian == 'no':
        print ('Main Street Pizza Company')
        print ("The Chef's Kithcen")
        print ('Corner Cafe')

    if gluten_free == 'no' and vegan == 'yes' and vegetarian == 'no':
         print ('Corner Cafe')
         print ("The Chef's Kithcen")

    if gluten_free == 'no' and vegan == 'no' and vegetarian == 'yes':
        print ('Corner Cafe')
        print ("The Chef's Kithcen")
        print ('Main Street Pizza Company')
        print ("Mama's Fine Italian")

    if gluten_free == 'yes' and vegan == 'yes' and vegetarian == 'no':
        print ('Corner Cafe')
        print ("The Chef's Kithcen")

    if gluten_free == 'no' and vegan == 'yes' and vegetarian == 'yes':
        print ('Corner Cafe')
        print ("The Chef's Kithcen")

    if gluten_free == 'yes' and vegan == 'no' and vegetarian == 'yes':
        print ('Main Street Pizza Company')
        print ("The Chef's Kithcen")
        print ('Corner Cafe')

    Search = input('Would you like to make a search? (Yes or No)')
    if Search == 'No':
        print ('There are no more searches to be made')
        break
    

    

    
    





