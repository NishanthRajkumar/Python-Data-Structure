'''
    @Author: Nishanth
    @Date: 05-04-2022 14:15:00
    @Last Modified by: Nishanth
    @Last Modified Date: 05-04-2022 14:15:00
    @Title: Convert user input to upper case and lower case
'''
import sys
import logging

def upper_lower_case():
    """
        Description:
            Convert user input to upper case and lower case
        
        Parameter:
            None
        
        Return:
            None
    """
    user_input = input("Enter any text: ")
    uppercase = user_input.upper()
    lowercase = user_input.lower()
    logging.info(f"Upper case: {uppercase}, lower case: {lowercase}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r'string_programs\string.log'), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    upper_lower_case()