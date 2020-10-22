def get_text_from_file(infile):
    """
    import text from the file specified by 'infile'
    remove punctuation
    split text into single word separated by white spaces
    return list of words
    """

    # get logger
    import logging
    logger = logging.getLogger()

    # read in text from file
    my_file = open(infile, "r")
    content = my_file.read()
    logger.debug("content", content)
    # remove punctuation
    content = content.replace('.', '')
    content = content.replace(',', '')
    content = content.replace(';', '')
    content = content.replace('!', '')
    # split content into words
    content_list = content.split(" ")
    my_file.close()
    logger.debug("content_list", content_list)

    return content_list


def compare_list_entry_with_previous_entries(list_with_content):
    """
    subsequently goes through the content of the given list and checks whether the entries have been used before in the
    list. A second list of the same length as the given list is created where that second list has the entries 'True'
    and 'False'. The entry 'True' indicates that the entry in the given list at the same position has been used before
    in that list and 'False' if it has not been used.
    The second list with 'True' and 'False' values is returned.
    """

    # get logger
    import logging
    logger = logging.getLogger()

    # logging the given values and its characteristics
    logger.debug("list_with_content: ", list_with_content)
    logger.debug("len(list_with_content): ", len(list_with_content))
    logger.debug("range(len(list_with_content)): ", range(len(list_with_content)))

    # create an empty list for a counter whether entries are repeated
    list_with_repetitions = [False] * len(list_with_content)
    # for each word in the list find out whether it has been used before in the text (True) or not (False)
    for i in range(len(list_with_content)):
        logger.debug("i=", i)
        for j in range(0, i):
            logger.debug("i=", i, "j=", j)
            if list_with_content[i] == list_with_content[j]:
                logger.debug("i=", i, "j=", j, "same", list_with_content[j])
                list_with_repetitions[i] = True
                break
    logger.debug(list_with_repetitions)

    return list_with_repetitions


def calculate_the_percentage_of_new_words(repetition_list):
    """
    go through all entries of the given list and calculate the respective percentage of new words up to this word.
    The given list must contain entries of 'True' and 'False', indicating a repeated word or new word respectively.
    A list of the same length as the given list is returned in which each entry has the percentage of new words up to
    the respective word in the given list.
    """

    # get logger
    import logging
    logger = logging.getLogger()

    # create a list of float numbers that will be filled with the percentage of new word up to the current word
    # to set up the "empty" list of float(!) numbers the value '0.0' is used
    # the length of the list is equal to the length of the given list
    list_with_repetition_numbers = [0.0] * len(repetition_list)
    logger.debug(list_with_repetition_numbers)
    # create a counter on how many repetitions occurred for each word
    repetition_counter = 0
    # go through all entries of the given list and calculate the respective percentage of new words up to this word
    for i in range(len(repetition_list)):
        if repetition_list[i] is False:
            repetition_counter += 1
        # divide the amount of current repetitions by the current number of words
        # multiplication by 100 to get percentage
        list_with_repetition_numbers[i] = 100*repetition_counter / (i+1)
    logger.debug(list_with_repetition_numbers)

    return list_with_repetition_numbers


def word_graphic(y_entries, file_name):
    """
    A simple line plot is generated in which the values of the given list is plotted against a running number.
    The x-axis is labeled 'words' and the y-axis 'percentage of new words' the title references the input file.
    The resulting figure is shown and saved as png file with the same name as the input file.
    """

    # get logger
    import logging
    logger = logging.getLogger()

    # import plot and math modules
    import matplotlib.pyplot as plt
    import numpy as np

    # check given entries
    logger.debug("y: ", y_entries)

    # for the x-axis simply a list of running number from 1 up to the total amount of entries is created
    x = np.arange(1, len(y_entries)+1)

    # the figure is set up and a simple line plot is generated from the given entry list
    fig, ax = plt.subplots()
    ax.plot(x, y_entries)

    # set axis label and title
    ax.set(xlabel='words',
           ylabel='percentage of new words',
           title='New word order of '+file_name)
    ax.grid()

    # plot graph and save it as png with the given filename
    fig.savefig(file_name+".png")
    plt.show()
