'''
    @Author: Nishanth
    @Date: 01-04-2022 22:41:00
    @Last Modified by: Nishanth
    @Last Modified Date: 01-04-2022 22:41:00
    @Title: concatenate dictionaries
'''
import logging
import sys

def concatenate_dict():
    """
        Description:
            concatenates 3 dictionaries
        
        Parameter:
            None
        Return:
            None
    """
    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50, 6:60}
    concatenated_dic = {}
    concatenated_dic.update(dic1)
    concatenated_dic.update(dic2)
    concatenated_dic.update(dic3)
    logging.info(f"Dictionary 1: {dic1}")
    logging.info(f"Dictionary 2: {dic2}")
    logging.info(f"Dictionary 3: {dic3}")
    logging.info(f"Concatenated dictionary: {concatenated_dic}")

if __name__ == '__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"dictionary_programs\dictionary.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    concatenate_dict()