'''
    @Author: Nishanth
    @Date: 03-04-2022 12:13:00
    @Last Modified by: Nishanth
    @Last Modified Date: 03-04-2022 12:13:00
    @Title: Compute length of list for dictionary values that are lists
'''
import logging
import sys

def compute_values_list_length(dict_data: dict):
    """
        Description:
            Checks if list of keys exist in dictionary
        
        Parameter:
            dict_data: a dictionary
            list_data: the list of keys
        
        Return:
            None
    """
    value_list_length = {}
    for key, value in dict_data.items():
        if type(value) is list:
            value_list_length[key] = len(value)
    if len(value_list_length) == 0:
        logging.warning("None of the values in dictionary were lists")
        return None
    logging.info(f"list length of values for keys with values as list: {value_list_length}")

if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"dictionary_programs\dictionary.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    sample_dict = {1: 'one', 2: 'two', 'Three': [3,4,5], 4: 'four', 5: [5,6,7,8]}
    compute_values_list_length(sample_dict)