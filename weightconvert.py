import pounds_or_kg
import math
import time
import weight

print(weight.weight_question)

conversion_rate = 0.45359237


def weight_convert():
    global conversion_rate
    conversion_rate = 0.45359237

    print("*************************************************")

    if weight >= 0:
        converted_weight = round((weight / conversion_rate), 1)
        print("*************************************************")
        if weight.weight_question >= 0:
            converted_weight = round((weight.weight_question / conversion_rate), 1)
            print("*************************************************")
            print(f'You weigh {converted_weight} pounds')
            weight_whole = math.floor(weight.weight_question.weight_convert())
            return weight_whole

    else:
        print("*************************************************")
        print("Please enter a valid weight")
        time.sleep(1)  # Delay for 2 second before restarting the loop
