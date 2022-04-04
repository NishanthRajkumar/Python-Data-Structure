'''
    @Author: Nishanth
    @Date: 04-04-2022 16:14:00
    @Last Modified by: Nishanth
    @Last Modified Date: 04-04-2022 16:14:00
    @Title: Find max and min of given set
'''
import sys
import logging

def max_min(set_data: set):
    """
        Description:
            Displays max and min of given set
        
        Parameter:
            set_data: a set, for max and min is computed
        
        Return:
            None
    """
    max_value = max(set_data)
    min_value = min(set_data)
    logging.info(f"The set is {set_data}")
    logging.info(f"The max value is {max_value}")
    logging.info(f"The min value is {min_value}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"set_programs\sets.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    sample_set = set([1, 2, 5, 78, 23, 3, 450, 48, 97, 98])
    max_min(sample_set)