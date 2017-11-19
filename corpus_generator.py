from collections import defaultdict

from nltk import trigrams
from nltk.corpus import gutenberg

gutenberg.fileids()


class CorpusGenerator(object):

    def __init__(self, path_to_txt_file):
        self.path_to_txt_file = path_to_txt_file

    def count_word_based_trigrams(self):
        """
        Creates a word-based trigram from a given text file.
        :return: a dictionary representing the appearance of each third word
        with respect to the two words before
        """
        try:
            word_based_model = defaultdict(lambda: defaultdict(lambda: 0))
            for sentence in gutenberg.sents(self.path_to_txt_file):
                for w1, w2, w3 in trigrams(sentence, pad_right=True, pad_left=True):
                    word_based_model[(w1, w2)][w3] += 1
            return word_based_model
        except ValueError as error:
            print(error)

    def count_char_based_trigrams(self):
        """
        creates a character-based trigram from a given text file
        :return: a dictionary representing the appearance of each third character
        with respect to the two characters before
        """
        char_based_model = defaultdict(lambda: defaultdict(lambda: 0))
        try:
            chars = gutenberg.raw(self.path_to_txt_file)
            # Initializing first characters and its appearance
            char_based_model[(None, None)][chars[0]] = 1
            char_based_model[(None, chars[0])][chars[1]] = 1
            for i in range(len(chars) - 3):
                char_based_model[(chars[i], chars[i+1])][chars[i+2]] += 1
            return char_based_model
        except ValueError as error:
            print(error)

    def calc_trigrams_probabilities(self, model):
        """
        :param model: a dictionary representing a trigram
        :return: a dictionary representing the trigrams probabilities
        """
        for w1_w2 in model:
            total_count = float(sum(model[w1_w2].values()))
            for w3 in model[w1_w2]:
                model[w1_w2][w3] /= total_count

    def create_word_based_language_model(self):
        """
        Creates a word-based language model based on probabilities of the trigram model.
        :return: A trigram (word based) language model as a dictionary
        """
        model = self.count_word_based_trigrams()
        self.calc_trigrams_probabilities(model)
        return model

    def create_char_based_language_model(self):
        """
        Creates a character-based language model based on probabilities of the trigram model.
        :return: A trigram (character based) language model as a dictionary
        """
        model = self.count_char_based_trigrams()
        self.calc_trigrams_probabilities(model)
        return model