import division_selector
import weight_cut_or_add

import weight_class_index
original_index_proper = None
new_index_proper = None
difference = None
def class_change():
    """This function is called after the weight_cut_or_add function. It runs a for loop on a weight class index for the
    original and new weights. We take the difference"""
    global original_index_proper, new_index_proper


    for key, value in weight_class_index.list_of_divisions.items():
        if division_selector.division_original in weight_class_index.list_of_divisions.keys():

            original_index = weight_class_index.list_of_divisions[division_selector.division_original]
            if original_index is not None:
                original_index_proper = original_index

            break

    for key, value in weight_class_index.list_of_divisions.items():
        if weight_cut_or_add.division_new in weight_class_index.list_of_divisions.keys():
            new_index= weight_class_index.list_of_divisions[weight_cut_or_add.division_new]
            if new_index is not None:
                new_index_proper = new_index
            break

#If functions to run based on the values of the indexes
    if new_index_proper>original_index_proper:
        global difference
        difference= new_index_proper - original_index_proper
        print("*************************************************")
        print(f'At your new weight you could go up {difference} division(s) and compete in the {weight_cut_or_add.division_new} division!')
        return difference
    elif original_index_proper>new_index_proper:
        #I have done the formula like this so the number is never negative in the statement
        difference = -new_index_proper + original_index_proper
        print("*************************************************")
        print(f'At your new weight you could go down {difference} division(s) and compete in the {weight_cut_or_add.division_new} division!')
        return difference
    else:
        print("*************************************************")
        print(f'At your new weight you would remain in the {weight_cut_or_add.division_new} division!')









