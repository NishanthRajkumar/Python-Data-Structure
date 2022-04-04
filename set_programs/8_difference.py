'''
    @Author: Nishanth
    @Date: 04-04-2022 15:00:00
    @Last Modified by: Nishanth
    @Last Modified Date: 04-04-2022 15:00:00
    @Title: Get the difference of multiple sets
'''
import sys
import logging

def set_diff(set1: set, set2: set, *sets: set):
    """
        Description:
            Gets the difference of multiple sets
        
        Parameter:
            set1: The first set to get difference from
            set2: The 2nd set for difference with set1
            sets: variable no of set parameter for difference with set1
        
        Return:
            None
    """
    difference_of_sets = set1.difference(set2)
    logging.info(f"Original sets:")
    logging.info(f"Set 1: {set1}")
    logging.info(f"Set 2: {set2}")
    for i in range(len(sets)):
        difference_of_sets = difference_of_sets.difference(sets[i])
        logging.info(f"Set {i+3}: {sets[i]}")
    logging.info(f"Difference of sets: {difference_of_sets}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"set_programs\sets.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    set1 = set([1, 2, 5, 78, 23, 3, 450, 48, 97, 98])
    set2 = set([3, 78, 1, 56])
    set3 = set([23, 48, 4, 3])
    set4 = set([28, 3, 98, 100])
    set_diff(set1, set2, set3, set4)