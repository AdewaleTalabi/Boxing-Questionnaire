from weight import weight
import math
import weight
import boxingDivisions
import femaleBoxingDivisions
import gender


def process_weight_type(value):
    result = value.upper()
    return result

def weight_option(type, c_a, weight, cut):
    """This function takes the values from the weight_change function to determine what the new weight class would be.
    There are two options cut or add, the new weight values are determined on the selected option, and another for loop
    is ran to determine the new weught"""
    new_weight = 0
    global new_weight_read

    if c_a == 'ADD':
        new_weight_read = round(weight + cut, 1)
        kg_new = round(new_weight_read / 2.20462, 0)
        shift_text = 'gain'
        new_weight = math.floor(weight + cut)
        global down_or_up
        down_or_up= 'up'


    if c_a == 'CUT':

        new_weight_read = round(weight - cut, 1)
        kg_new = round(new_weight_read / 2.20462, 0)
        shift_text = 'cut'
        new_weight = math.floor(weight - cut)
        down_or_up = 'down'


    if gender.gender_type in ['MALE', 'M']:
        for division, value in boxingDivisions.list_of_divisions.items():
            if new_weight in value:
                print("*************************************************")
                weight_statement = print(f'After your {weight_shift} {type} {shift_text}, your new weight would be approximately: {new_weight_read} pounds ({kg_new} kg)')
                global division_new
                division_new= division
                return division_new

    if gender.gender_type in ['FEMALE', 'F']:
        for division, value in femaleBoxingDivisions.list_of_divisions.items():
            if new_weight in value:
                print("*************************************************")
                weight_statement = print(f'After your {weight_shift} {type} {shift_text}, your new weight would be approximately: {new_weight_read} pounds ({kg_new} kg)')
                division_new = division
                return division_new

    return


def weight_change():
    #This function asks users whether they want to increase or decrease their current weight to change fight class
    global kg_new, new_weight_read,shift_text,weight_shift,original_weight

    original_weight = weight.weight_result
    p_or_kg = weight.pounds_or_kg

    while True:
        print("*************************************************")
        weight_change = input("Are you willing to cut or add weight? Please enter Add or Cut: ").upper()

        wc_lower = weight_change
        if weight_change in ['ADD', 'CUT']:

            while True:
                try:
                    print("*************************************************")
                    weight_shift = int(input(f'How much weight are you willing to {weight_change.lower()}? Please enter a POSITIVE whole number: '))
                except ValueError:
                    print("*************************************************")
                    print("Weight cannot contain words!")
                    print("*************************************************")
                    weight_shift = int(input(f'How much weight are you willing to {weight_change.lower()}? Please enter a POSITIVE whole number: '))


                finally:
                    if weight_shift>0:

                        global cut_converted
                        cut_converted = (weight_shift / 0.453593855958196)

                        if cut_converted > original_weight and weight_change == 'CUT':
                            print("*************************************************")
                            print("Weight cut cannot be greater than current weight!")
                            continue

                        elif cut_converted > 0:
                            if p_or_kg in ['KGS', 'KILOGRAMS', 'KG', 'K']:
                                global type_of_m
                                type_of_m = "kg"
                                weight_option(type_of_m, wc_lower, original_weight, cut_converted)
                                return

                            if p_or_kg in ['POUNDS', 'LBS', 'LB', 'P']:
                                type_of_m = "lbs"
                                cut_converted = (weight_shift / 1)
                                weight_option(type_of_m,wc_lower,original_weight,cut_converted)
                                return
                    else:
                        print("*************************************************")
                        print("Integer cannot be negative!")

        else:
            print("*************************************************")
            print("Insert valid option!")
