'''
    @Author: Nishanth
    @Date: 05-04-2022 13:27:00
    @Last Modified by: Nishanth
    @Last Modified Date: 05-04-2022 13:27:00
    @Title: Find longest word in list
'''
import sys
import logging

def longest_word(list_of_words: list[str]):
    """
        Description:
            Retrieves the longest word in list
        
        Parameter:
            list_of_words: list of str type items
        
        Return:
            None
    """
    logging.info(f"List of words: {list_of_words}")
    biggest_word = ""
    for word in list_of_words:
        if len(word) > len(biggest_word):
            biggest_word = word
    logging.info(f"First occurence of longest length word is '{biggest_word}' of length {len(biggest_word)}")

if __name__=='__main__':
    logging.basicConfig(handlers=[logging.FileHandler(r'string_programs\string.log'), logging.StreamHandler(sys.stdout)], level=logging.INFO)
    sample_list = ['list', 'tuple', 'array', 'string', 'dictionary', 'set']
    longest_word(sample_list)