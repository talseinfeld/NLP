import random

from corpus_generator import CorpusGenerator


def generate_random_word_based(path, words):

    model = CorpusGenerator(path).create_word_based_language_model()
    text = [None, None]

    for _ in range(int(words)):
        r = random.random()
        accumulator = .0
        for word in model[tuple(text[-2:])].keys():
            accumulator += model[tuple(text[-2:])][word]

            if accumulator >= r:
                text.append(word)
                break
    file = open("Random Generated Text.txt", 'w')
    file.write(' '.join([t for t in text if t]))
    file.close()
    print(' '.join([t for t in text if t]))


def generate_random_char_based(path, words):

    model = CorpusGenerator(path).create_char_based_language_model()
    text = [None, None]

    for _ in range(int(words)):
        r = random.random()
        accumulator = .0
        for word in model[tuple(text[-2:])].keys():
            accumulator += model[tuple(text[-2:])][word]

            if accumulator >= r:
                text.append(word)
                break
    file = open("Random Generated Text.txt", 'w')
    file.write(''.join([t for t in text if t]))
    file.close()
    print(''.join([t for t in text if t]))

