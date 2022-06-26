'''
    @Author: Nishanth
    @Date: 02-04-2022 10:44:00
    @Last Modified by: Nishanth
    @Last Modified Date: 02-04-2022 10:44:00
    @Title: Iterate over a dictionary using for loop
'''
import logging
import sys

def iterate_dic(dictionary_to_iterate: dict):
    """
        Description:
            Iterates over a dictionary using for loop
        
        Parameter:
            Accepts a dictionary as parameter
        
        Return:
            None
    """
    logging.info("Iterating over Dictionary:")
    for item in dictionary_to_iterate.items():
        logging.info(f"[{item[0]}: {item[1]}]")

if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"dictionary_programs\dictionary.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    sample_dictionary = {1: 230, 2: 350, 3: 130}
    iterate_dic(sample_dictionary)