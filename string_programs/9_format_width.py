'''
    @Author: Nishanth
    @Date: 05-04-2022 14:50:00
    @Last Modified by: Nishanth
    @Last Modified Date: 05-04-2022 14:50:00
    @Title: display formatted text (width=50) as output
'''
import sys
import logging

def format_width():
    """
        Description:
            Displays formatted text (width=50) as output
        
        Parameter:
            None
        
        Return:
            None
    """
    user_txt = input("Enter any txt: ")
    logging.info(f"Formatted text (width = 50):\n{user_txt:>50}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r'string_programs\string.log'), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    format_width()