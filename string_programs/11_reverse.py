'''
    @Author: Nishanth
    @Date: 05-04-2022 14:50:00
    @Last Modified by: Nishanth
    @Last Modified Date: 05-04-2022 14:50:00
    @Title: Reverse a string
'''
import sys
import logging

def reverse():
    """
        Description:
            Reverse a string
        
        Parameter:
            None
        
        Return:
            None
    """
    user_text = input("Enter any text: ")
    reverse_txt = user_text[::-1]
    logging.info(f"Reversed text: {reverse_txt}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r'string_programs\string.log'), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    reverse()