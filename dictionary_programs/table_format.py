'''
    @Author: Nishanth
    @Date: 02-04-2022 11:36:00
    @Last Modified by: Nishanth
    @Last Modified Date: 02-04-2022 11:36:00
    @Title: Print dictionary in table format
'''
import logging
import sys

def table_format(dictionary_data: dict):
    """
        Description:
            Prints dictionary in table format
        
        Parameter:
            accepts a dictionary
        
        Return:
            None
    """
    logging.info("{:<7}| {:<10}".format('Key', 'Value'))
    for key, value in dictionary_data.items():
        logging.info("{:<7}| {:<10}".format(key, value))

if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"dictionary_programs\dictionary.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    sample_dict = {'1st': 1234, '2nd': 'qwer', 3: 5+7j}
    table_format(sample_dict)