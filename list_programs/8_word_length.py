'''
    @Author: Nishanth
    @Date: 05-04-2022 07:30:00
    @Last Modified by: Nishanth
    @Last Modified Date: 05-04-2022 07:30:00
    @Title: Get list of words that are longer than n from a given list of words
'''
from copy import deepcopy
import sys
import logging

def word_length_filter(list_of_words: list[str]):
    """
        Description:
            find words in list that are longer than n(specified by user)
        
        Parameter:
            list_of_words: a list string type objects
        
        Return:
            None
    """
    filtered_word_list = []
    logging.info(f"The given list of words: {list_of_words}")
    word_length = int(input(f"Enter min word length: "))
    for word in list_of_words:
        if type(word) is str and len(word) >= word_length:
            filtered_word_list.append(word)
    logging.info(f"Words with length > {word_length}: {filtered_word_list}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r"list_programs\list_programs.log"), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    word_length_filter(['shell', 'powershell', 'gitbash', 'terminal', 'cmd'])