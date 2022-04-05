'''
    @Author: Nishanth
    @Date: 05-04-2022 12:26:00
    @Last Modified by: Nishanth
    @Last Modified Date: 05-04-2022 12:26:00
    @Title: Slice a tuple
'''
import sys
import logging

def slice_tuple(tuple_data: tuple, index: int = None):
    """
        Description:
            Removes item from tuple
        
        Parameter:
            tuple_data: a tuple
            index: The index value to slice at
        
        Return:
            None
    """
    logging.info(f"Original Tuple: {tuple_data}")
    if index == None:
        try:
            index = int(input("Enter index to slice at: "))
        except:
            logging.error("Invalid index")
            return None
    if index >= len(tuple_data):
        logging.error("Index must be > 0 and < length of tuple")
        return None
    tuple1 = tuple_data[:index]
    tuple2 = tuple_data[index:]
    logging.info(f"After slicing at {index}\nTuple 1: {tuple1}\nTuple 2: {tuple2}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"tuple_programs\tuple_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    slice_tuple(['rgb', 70, 30, 49, 'rgb', 30, 30, 70], 4)