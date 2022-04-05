'''
    @Author: Nishanth
    @Date: 05-04-2022 11:43:00
    @Last Modified by: Nishanth
    @Last Modified Date: 05-04-2022 11:43:00
    @Title: Find repeated items of tuple
'''
import sys
import logging

def find_repeated(tuple_data: tuple):
    """
        Description:
            Finds repeated items of tuple
        
        Parameter:
            tuple_data: A tuple
        
        Return:
            None
    """
    repeated_tuple_items = {}
    for item in tuple_data:
        if tuple_data.count(item) > 1:
            repeated_tuple_items[item] = tuple_data.count(item)
    logging.info(f"Original tuple: {tuple_data}")
    logging.info(f"Repeated tuple items: {repeated_tuple_items}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"tuple_programs\tuple_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    find_repeated(('rgb', 70, 30, 49, 'rgb', 30, 30, 70))