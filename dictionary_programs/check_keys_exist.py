'''
    @Author: Nishanth
    @Date: 03-04-2022 12:01:00
    @Last Modified by: Nishanth
    @Last Modified Date: 03-04-2022 12:01:00
    @Title: Check if list of keys exist in dictionary
'''
import logging
import sys

def check_keys_exist(dict_data: dict, list_of_keys: list):
    """
        Description:
            Checks if list of keys exist in dictionary
        
        Parameter:
            dict_data: a dictionary
            list_data: the list of keys
        
        Return:
            None
    """
    keys_set = set(list_of_keys)
    if keys_set.issubset(dict_data.keys()):
        logging.info(f"The keys ({keys_set}) are present in dictionary: {dict_data}")
    else:
        logging.info(f"The keys ({keys_set}) are not all present in dictionary: {dict_data}")

if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"dictionary_programs\dictionary.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    sample_dict = {1: 'one', 2: 'two', 3: 'foo', 4: 'four', 5: 'bar'}
    check_keys_exist(sample_dict, [1, 3, 5])