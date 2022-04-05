'''
    @Author: Nishanth
    @Date: 05-04-2022 12:59:00
    @Last Modified by: Nishanth
    @Last Modified Date: 05-04-2022 12:59:00
    @Title: Compute string length
'''
import sys
import logging

def str_len(text: str):
    """
        Description:
            Computes string length
        
        Parameter:
            text: any string text
        
        Return:
            None
    """
    logging.info(f"The length of {text} is {len(text)}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r'string_programs\string.log'), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    str_len("Visual Studio Code")