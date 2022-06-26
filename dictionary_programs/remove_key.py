'''
    @Author: Nishanth
    @Date: 02-04-2022 11:07:00
    @Last Modified by: Nishanth
    @Last Modified Date: 02-04-2022 11:07:00
    @Title: Remove key from dictionary
'''
import logging
import sys

def remove_key(dictionary_to_update: dict, key):
    """
        Description:
            Removes key from dictionary
        
        Parameter:
            dictionary_to_update: the dictionary to remove the key from
            key: The value of key to be removed
        
        Return:
            None
    """
    if key not in dictionary_to_update.keys():
        logging.error("The key does not exist in dictionary")
        return None
    logging.info(f"Orginal dictionary: {dictionary_to_update}")
    del dictionary_to_update[key]
    logging.info(f"Updated dictionary: {dictionary_to_update}")

if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"dictionary_programs\dictionary.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    sample_dictionary = {1: 230, 2: 350, 3: 130}
    remove_key(sample_dictionary, 2)