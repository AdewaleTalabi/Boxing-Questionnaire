import math
import time

weight_result = None
pounds_or_kg = None

def weight():
    # This is the overall function that will get called by the in the other files, i.e. division selector
    global weight_whole
    global weight_result
    weight_result = weight_proper()
    return weight_result

def weight_type():
    '''This function will ask for what kind of metric the user is putting in.
    The function will conduct data validation, and correct type is not put in will ask again'''
    while True:
        print("*************************************************")
        global pounds_or_kg
        pounds_or_kg = input('Enter weight type: ').upper()

        if pounds_or_kg not in ['KGS', 'KILOGRAMS', 'KG', 'K', 'POUNDS', 'LBS', 'LB', 'P']:
            print("*************************************************")
            print("Enter valid weight type!")
            continue
        else:
            #time.sleep(1)
            return pounds_or_kg

def kg_weight_converter(kgs):
    # This function converts the weight of any kg values into pounds

    converted_weight = round((kgs / 0.45359237), 1)
    print("*************************************************")
    print(f'You weigh {converted_weight} pounds')
    weight_whole = math.floor(converted_weight)
    return weight_whole

def weight_proper():
    '''This function will take the weight type answer.
    It will ask users for their weight, and depending on the weight type, will perform a conversion.
    The function contains validations to catch any words that maybe put inside the weight answer.
    Function contains validation to prevent negative weight values'''
    p_or_k = weight_type()
    while True:

        print("*************************************************")
        try:

            weight_question = float(input("Enter weight: "))
        except ValueError:
            print("*************************************************")
            print("Weight cannot contain words!")
            continue

        if weight_question > 0:

            if p_or_k in ['KGS', 'KILOGRAMS', 'KG', 'K']:

                kg_weight = kg_weight_converter(weight_question)
                weight_whole = math.floor(kg_weight)
                return weight_whole


            elif p_or_k in ['POUNDS', 'LBS', 'LB', 'P']:
                pounds = weight_question
                print("*************************************************")
                print(f'You weigh {pounds} pounds')
                weight_whole = math.floor(weight_question)
                return weight_whole

        if weight_question < 0:
                print("*************************************************")
                print("Weight cannot be negative!")
                continue

