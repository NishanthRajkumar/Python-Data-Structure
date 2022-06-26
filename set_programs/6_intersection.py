'''
    @Author: Nishanth
    @Date: 04-04-2022 13:06:00
    @Last Modified by: Nishanth
    @Last Modified Date: 04-04-2022 13:06:00
    @Title: Get the intersection of multiple sets
'''
import sys
import logging

def set_intersection(set1: set, set2: set, *sets: set):
    """
        Description:
            Gets the intersection of multiple sets
        
        Parameter:
            set1: The first set to intersect
            set2: The 2nd set to intersect
            sets: variable no of set parameter to intersect
        
        Return:
            None
    """
    intersection_of_sets = set1.intersection(set2)
    logging.info(f"Original sets:")
    logging.info(f"Set 1: {set1}")
    logging.info(f"Set 2: {set2}")
    for i in range(len(sets)):
        intersection_of_sets = intersection_of_sets.intersection(sets[i])
        logging.info(f"Set {i+3}: {sets[i]}")
    logging.info(f"intersection of sets: {intersection_of_sets}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"set_programs\sets.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    set1 = set([1, 2, 5, 78, 23, 3])
    set2 = set([3, 78, 1, 5])
    set3 = set([23, 78, 1, 3])
    set4 = set([23, 3, 78, 1])
    set_intersection(set1, set2, set3, set4)