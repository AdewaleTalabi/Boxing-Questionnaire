import pounds_or_kg
import math
import weight

from BoxingProject import boxingDivisions
from BoxingProject.boxingDivisionCalc import converted_weight


def weight_change():

    weight_shift = input("Are you willing to cut or add weight? Please enter Add or Cut: ").upper()
    if weight_shift in ['ADD']:
        print("*************************************************")
        weight_shift = int(input('How much weight are you willing to add? Please enter a whole number '))
        if pounds_or_kg in ['KGS', 'KILOGRAMS', 'KG', 'K']:
            cut_converted = (weight_shift / 0.45)

            new_weight_read = round(converted_weight + cut_converted, 1)
            new_weight = math.floor(converted_weight + cut_converted)
            print("*************************************************")
            print(f'Your new weight would be: {new_weight_read} pounds')
            for division, value in boxingDivisions.list_of_divisions.items():
                if new_weight in value:
                    print("*************************************************")
                    print(f'After your weight gain, you could compete in the male {division} division!')

        elif pounds_or_kg in ['POUNDS', 'LBS', 'LB', 'P']:
            print("*************************************************")
            new_weight = math.floor(weight.weight() + weight_shift)
            print(f'Your new weight would be: {new_weight} pounds')

            for division, value in boxingDivisions.list_of_divisions.items():
                if new_weight in value:
                    print("*************************************************")
                    print(f'After your weight gain, you could compete in the male {division} division!')

                    break

    if weight_shift in ['CUT']:
        print("*************************************************")
        weight_shift = int(input('How much weight are you willing to cut? Please enter a whole number: '))
        if weight_shift > 0:
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
                new_weight = math.floor(weight.weight() - weight_shift)
                print(f'Your new weight would be: {new_weight} pounds')

                for division, value in boxingDivisions.list_of_divisions.items():
                    if new_weight in value:
                        print("*************************************************")
                        print(f'After your weight cut, you could compete in the male {division} division!')

                        break
            else:
                print("*************************************************")
                print("Please enter valid option")

        else:
            print("*************************************************")
            print("Please enter a valid number")
