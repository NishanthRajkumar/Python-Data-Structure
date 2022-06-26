'''
    @Author: Nishanth
    @Date: 01-04-2022 22:41:00
    @Last Modified by: Nishanth
    @Last Modified Date: 01-04-2022 22:41:00
    @Title: Add a key to dictionary
'''
import logging
import sys

def add_key(dictionary_to_update: dict, key, value = None):
    """
        Description:
            Adds a key to dictionary.
            Can optionally give value for the key
        
        Parameter:
            dictionary_to_update: dictionary to add the key
            key: the key to be added
            value: value for the corresponding key. Default: None
        
        Return:
            None
    """
    if key in dictionary_to_update.keys():
        logging.error(f"Key={key} already exists")
        return None
    logging.info(f"Orginal Dictionary: {dictionary_to_update}")
    dictionary_to_update[key] = value
    logging.info(f"After adding key: {dictionary_to_update}")

if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"dictionary_programs\dictionary.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    sample_dictionary = {1: 230, 2: 350, 3: 130}
    add_key(sample_dictionary, '4th', 267)
    add_key(sample_dictionary, '5th')
    add_key(sample_dictionary, '5th')