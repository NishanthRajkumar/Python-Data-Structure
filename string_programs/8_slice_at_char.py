'''
    @Author: Nishanth
    @Date: 05-04-2022 14:32:00
    @Last Modified by: Nishanth
    @Last Modified Date: 05-04-2022 14:32:00
    @Title: Gets the last part of a string before a specified character
'''
import sys
import logging

def slice_at_char(text: str):
    """
        Description:
            Gets the last part of a string before a specified character
        
        Parameter:
            text: any string text
        
        Return:
            None
    """
    logging.info(f"Original text: {text}")
    split_char = input("Enter a char from above text to get sliced text: ")
    if len(split_char) != 1:
        logging.error("Input char must be a single char only")
        return None
    text_result = text.split(split_char, maxsplit=1)[0]
    logging.info(f"Sliced text: {text_result}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r'string_programs\string.log'), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    slice_at_char('https://www.w3resource.com/python-exercises')