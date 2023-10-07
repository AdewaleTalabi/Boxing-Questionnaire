import math
import time
import boxingDivisions
import femaleBoxingDivisions

weight = 0
converted_weight = 0
valid_weight_type = True


while True:
    print("*************************************************")
    gender = input("Enter gender: ").upper()
    if gender in ['MALE', 'M']:
        print("*************************************************")
        pounds_or_kg = input('Enter weight type: ').upper()

        if pounds_or_kg in ['KGS', 'KILOGRAMS', 'KG', 'K']:
            print("*************************************************")
            weight = float(input('Enter weight: '))
            if weight >= 0:
                converted_weight = round((weight / 0.45), 1)
                print("*************************************************")
                print(f'You weigh {converted_weight} pounds')
                weight = math.floor(converted_weight)




            else:
                print("*************************************************")
                print("Please enter a valid weight")
                time.sleep(1)  # Delay for 2 second before restarting the loop
                break

        elif pounds_or_kg in ['POUNDS', 'LBS', 'LB', 'P']:
            print("*************************************************")
            weight_pounds = round(float(input('Enter weight: ')),2)
            weight = math.floor(weight_pounds)

            if weight >= 0:
                print("*************************************************")
                print(f'You weigh {weight_pounds} pounds')


            else:
                print("*************************************************")
                print("Please enter a valid weight")
                time.sleep(1)  # Delay for 2 second before restarting the loop
                continue

        else:
            print("*************************************************")
            print("Enter valid weight type!")
            time.sleep(1)  # Delay for 2 second before restarting the loop
            valid_weight_type = False

        if pounds_or_kg in ['KGS', 'KILOGRAMS', 'KG', 'K', 'POUNDS', 'LBS', 'LB', 'P']:
            for division, value in boxingDivisions.list_of_divisions.items():
                if weight in value:
                    print("*************************************************")
                    print(f'At your current weight, you can compete in the male {division} division!')
                    time.sleep(2)
                    print("*************************************************")
                    weight_change = input("Are you willing to cut or add weight? Please enter Add or Cut: ").upper()
                    if weight_change in ['ADD']:
                        print("*************************************************")
                        weight_shift = int(input('How much weight are you willing to add? Please enter a whole number '))
                        if pounds_or_kg in ['KGS', 'KILOGRAMS', 'KG', 'K']:
                            cut_converted = (weight_shift / 0.45)

                            new_weight_read = round(converted_weight+cut_converted,1)
                            new_weight = math.floor(converted_weight + cut_converted)
                            print("*************************************************")
                            print(f'Your new weight would be: {new_weight_read} pounds')
                            for division, value in boxingDivisions.list_of_divisions.items():
                                if new_weight in value:
                                    print("*************************************************")
                                    print(f'After your weight gain, you could compete in the male {division} division!')

                        elif pounds_or_kg in ['POUNDS', 'LBS', 'LB', 'P']:
                            print("*************************************************")
                            new_weight = math.floor(weight + weight_shift)
                            print(f'Your new weight would be: {new_weight} pounds')

                            for division, value in boxingDivisions.list_of_divisions.items():
                                if new_weight in value:
                                    print("*************************************************")
                                    print(f'After your weight gain, you could compete in the male {division} division!')

                                    break




                    if weight_change in ['CUT']:
                        print("*************************************************")
                        weight_shift = int(input('How much weight are you willing to cut? Please enter a whole number: '))
                        if weight_shift >0:
                            if pounds_or_kg in ['KGS', 'KILOGRAMS', 'KG', 'K']:
                                cut_converted = (weight_shift / 0.45)

                                new_weight_read = round(converted_weight - cut_converted, 1)
                                new_weight = math.floor(converted_weight - cut_converted)
                                print("*************************************************")
                                print(f'Your new weight would be: {new_weight_read} pounds')
                                for division, value in boxingDivisions.list_of_divisions.items():
                                    if new_weight in value:
                                        print("*************************************************")
                                        print(f'After your weight gain, you could compete in the male {division} division!')

                            elif pounds_or_kg in ['POUNDS', 'LBS', 'LB', 'P']:
                                print("*************************************************")
                                new_weight = math.floor(weight - weight_shift)
                                print(f'Your new weight would be: {new_weight} pounds')

                                for division, value in boxingDivisions.list_of_divisions.items():
                                    if new_weight in value:
                                        print("*************************************************")
                                        print(f'After your weight cut, you could compete in the male {division} division!')

                                        break
                            else:
                                print("*************************************************")
                                print("Please enter valid option")
                                continue
                        else:
                            print("*************************************************")
                            print("Please enter a valid number")

    elif gender in ['FEMALE','F']:
        print("*************************************************")
        pounds_or_kg = input('Enter weight type: ').upper()

        if pounds_or_kg in ['KGS', 'KILOGRAMS', 'KG', 'K']:
            print("*************************************************")
            weight = float(input('Enter weight '))
            if weight >= 0:
                converted_weight = round((weight / 0.45), 1)
                print("***********************")
                print(f'You weigh {converted_weight} pounds')
                weight = math.floor(converted_weight)



            else:
                print("*************************************************")
                print("Please enter a valid weight")
                time.sleep(1)  # Delay for 2 second before restarting the loop
                break
        else:
            print("*************************************************")
            print("Enter valid weight type!")
            time.sleep(1)  # Delay for 2 second before restarting the loop
            valid_weight_type = False

        if valid_weight_type:
            for division, value in femaleBoxingDivisions.list_of_divisions.items():
                if weight in value:
                    print("*************************************************")
                    print(f'At your current weight, you can compete in the male {division} division!')
                    time.sleep(2)
                    print("*************************************************")
                    weight_change = input("Are you willing to cut weight? Please enter yes or no ").upper()
                    if weight_change in ['YES', 'Y', 'YEAH']:
                        print("*************************************************")
                        weight_shift = int(input('How much weight are you willing to cut? Please enter a whole number '))
                        new_weight = weight - weight_shift
                        for division, value in femaleBoxingDivisions.list_of_divisions.items():
                            if new_weight in value:
                                print("*************************************************")
                                print(f'After your weight cut, you could compete in the female {division} division!')
    else:
        print("*************************************************")
        print("Enter valid gender")
        time.sleep(1)  # Delay for 2 second before restarting the loop
        continue
