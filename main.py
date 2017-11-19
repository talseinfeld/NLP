import sys

import text_generator


def main(path, word_base, total_words):
    if word_base == 'char':
        text_generator.generate_random_char_based(path, total_words)
    elif word_base == 'word':
        text_generator.generate_random_word_based(path, total_words)
    else:
        raise ValueError('You need to choose between char based module or word based.')


if __name__ == '__main__':
    """
    Make sure you download the gutenberg package.
    If you want to use any additional text, feel free to just add it to the gutenberg
    directory.
    """
    try:
        path_to_txt_file = sys.argv[1]
        word_base = sys.argv[2]
        words = sys.argv[3]
        main(path_to_txt_file, word_base, words)
    except ValueError as error:
        print(error)
