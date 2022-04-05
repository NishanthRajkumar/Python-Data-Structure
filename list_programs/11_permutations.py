'''
    @Author: Nishanth
    @Date: 05-04-2022 07:46:00
    @Last Modified by: Nishanth
    @Last Modified Date: 05-04-2022 07:46:00
    @Title: get all permutations of a list
'''
import sys
import logging
from itertools import permutations

def list_permutations(list_data: list):
    """
        Description:
            Gets all permutations of a list
        
        Parameter:
            list_data: The list to find permutation for
        
        Return:
            None
    """
    lists = permutations(list_data)
    logging.info(f"Orginal list: {list_data}")
    logging.info(f"list permutations:")
    count = 1
    for sublist in lists:
        logging.info(f"Permutation {count}: {sublist}")
        count+=1

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"list_programs\list_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    sample_list = ['powershell', 'gitbash', 'terminal']
    list_permutations(sample_list)