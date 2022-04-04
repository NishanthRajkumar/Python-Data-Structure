'''
    @Author: Nishanth
    @Date: 04-04-2022 15:16:00
    @Last Modified by: Nishanth
    @Last Modified Date: 04-04-2022 15:16:00
    @Title: clear the given set
'''
import sys
import logging

def set_clear(set_data: set):
    """
        Description:
            clears the given set
        
        Parameter:
            set_data: the set to be cleared
        
        Return:
            None
    """
    logging.info(f"The set before clearing: {set_data}")
    set_data.clear()
    logging.info(f"The set after clearing: {set_data}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"set_programs\sets.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    sample_set = set([1, 2, 5, 78, 23, 3, 450, 48, 97, 98])
    set_clear(sample_set)