'''
    @Author: Nishanth
    @Date: 04-04-2022 15:08:00
    @Last Modified by: Nishanth
    @Last Modified Date: 04-04-2022 15:08:00
    @Title: Compute the symmetric difference of multiple sets
'''
import sys
import logging

def set_symm_diff(set1: set, set2: set, *sets: set):
    """
        Description:
            Computes the symmetric difference of multiple sets
        
        Parameter:
            set1: 1st mandatory parameter to compute symm diff amongst all given sets
            set2: 2nd mandatory parameter to compute symm diff amongst all given sets
            sets: variable no of set parameter to compute symm diff with all provided sets
        
        Return:
            None
    """
    symm_diff_of_sets = set1.symmetric_difference(set2)
    logging.info(f"Original sets:")
    logging.info(f"Set 1: {set1}")
    logging.info(f"Set 2: {set2}")
    for i in range(len(sets)):
        symm_diff_of_sets = symm_diff_of_sets.symmetric_difference(sets[i])
        logging.info(f"Set {i+3}: {sets[i]}")
    logging.info(f"Symmetric Difference of sets: {symm_diff_of_sets}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"set_programs\sets.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    set1 = set([1, 2, 5, 78, 23, 3, 450, 48, 97, 98])
    set2 = set([3, 78, 1, 56])
    set3 = set([23, 48, 4, 3])
    set4 = set([28, 3, 98, 100])
    set_symm_diff(set1, set2, set3, set4)