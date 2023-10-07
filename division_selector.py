import time

import boxingDivisions
import femaleBoxingDivisions
import gender
import weight
division_original = None
fbd = femaleBoxingDivisions.list_of_divisions.items()
def division_selector():
    global division_original
    gen_gen = gender.gender()
    wey_wey = weight.weight()

    if gen_gen in ['MALE', 'M']:
        for division, value in boxingDivisions.list_of_divisions.items():
            if wey_wey in value:
                print("*************************************************")
                division_statement = print(f'At your current weight, you can compete in the male {division} division!')

                division_original= division
                return (division_statement), division_original
                #time.sleep(2)
    elif gen_gen in ['FEMALE', 'F']:
        for division, value in femaleBoxingDivisions.list_of_divisions.items():
            if wey_wey in value:
                print("*************************************************")
                division_statement = print(f'At your current weight, you can compete in the female {division} division!')
                division_original = division
                return (division_statement), division_original
                #time.sleep(2)
        print("*************************************************")
        print("Enter valid gender")
        time.sleep(1)  # Delay for 2 second before restarting the loop
#division_selector()