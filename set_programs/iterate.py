'''
    @Author: Nishanth
    @Date: 03-04-2022 21:47:00
    @Last Modified by: Nishanth
    @Last Modified Date: 03-04-2022 21:47:00
    @Title: Iterate over a set
'''
import sys
import logging

def iterate(list_of_sets: list[set]):
    """
        Description:
            Iterate over given data set and print values
        
        Parameter:
            set_data: the list of set data to iterate over
        
        Return:
            None
    """
    count = 0
    for set_item in list_of_sets:
        if type(set_item) != set:
            logging.error("Not all the items inside the list were sets")
        count+=1
        logging.info(f"Set {count}: {set_item}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"set_programs\sets.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    iterate([set(['asd', 'qwe']), set(['fgh', 'rty'])])