'''
    @Author: Nishanth
    @Date: 02-04-2022 11:16:00
    @Last Modified by: Nishanth
    @Last Modified Date: 02-04-2022 11:16:00
    @Title: retreive unique values from dictionary
'''
import logging
import sys

def unique_values(dictionary_data: dict):
    """
        Description:
            retreive unique set of values from dictionary
        
        Parameter:
            dictionary_data: the dictionary to retreive unique set of values from
        
        Return:
            None
    """
    unique_dict_values = set()
    for _, value in dictionary_data.items():
        unique_dict_values.add(value)
    logging.info(f"The dictionary provided: {dictionary_data}")
    logging.info(f"Unque set of values: {unique_dict_values}")

if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"dictionary_programs\dictionary.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    sample_dictionary = {"V":"S001", "V": "S002", "VI": "S001", "VI": "S005", "VII":"S005", "V":"S009", "VIII":"S007"}
    unique_values(sample_dictionary)