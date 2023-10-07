import math
import time
import boxingDivisions
import femaleBoxingDivisions

gender_type = None
def gender():


    while True:

        global gender_type

        print("*************************************************")
        gender_type = input("Enter gender: ").upper()
        if gender_type in ['MALE', 'M']:
            return gender_type


        elif gender_type in ['FEMALE', 'F']:
            return gender_type
        else:
            print("*************************************************")
            print("Enter valid gender!")
            time.sleep(1)  # Delay for 2 second before restarting the loop
#gender()

