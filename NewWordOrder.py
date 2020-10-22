""" Program to make a visual representation of the distribution of new words in a given text """
from NewWordOrder_subroutines import get_text_from_file
from NewWordOrder_subroutines import compare_list_entry_with_previous_entries
from NewWordOrder_subroutines import word_graphic
from NewWordOrder_subroutines import calculate_the_percentage_of_new_words
import logging


def main():
    """ Controls the main flow

    The program has three main subroutines
    1: read in text from a file/source
    1b: transform text into list
    2: compare each word in list with previous words
    2b: add a counter depending on whether the word is new or not
    3: create a graph showing the distribution of new words in the text
    """

    # create and configure logger
    logging.basicConfig(filename="NewWordOrder.log", level=logging.ERROR, filemode='w')
    logger = logging.getLogger()

    # Name of the text file to be analysed
    infile = "Die_Glocke.txt"

    " Part 1: read in list and transform into a list"
    word_list = get_text_from_file(infile)
    logger.debug("main", "word_list: ", word_list)

    " Part 2: compare each word in list with previous words"
    # for each word in the list find out whether it has been used before in the text (True) or not (False)
    repetition_list = compare_list_entry_with_previous_entries(word_list)
    logger.debug("repetition_list:", repetition_list)
    # for each word calculate the percentage of new words in the text up to the place of this word
    list_with_repetition_numbers = calculate_the_percentage_of_new_words(repetition_list)
    logger.debug("list_with_repetition_numbers:", list_with_repetition_numbers)

    " Part 3: create a graph showing the distribution of new words in the text"
    # create a graph in which the percentage of new word is plotted against the current word
    word_graphic(list_with_repetition_numbers, infile)


if __name__ == '__main__':
    main()
