'''
    @Author: Nishanth
    @Date: 05-04-2022 14:50:00
    @Last Modified by: Nishanth
    @Last Modified Date: 05-04-2022 14:50:00
    @Title: count occurrences of a substring in a string
'''
import sys
import logging

def count_substr(text: str):
    """
        Description:
            counts occurrences of a substring in a string
        
        Parameter:
            None
        
        Return:
            None
    """
    logging.info(f"Original text: {text}")
    substring = input("Enter substring: ")
    substr_count = text.count(substring)
    logging.info(f"The substring occurs {substr_count} times")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r'string_programs\string.log'), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    count_substr("geeks for geeks")