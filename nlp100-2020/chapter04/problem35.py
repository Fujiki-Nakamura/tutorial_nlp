from collections import defaultdict
import pprint

from problem30 import parse


pp = pprint.PrettyPrinter()


def calc_word_frequency(parsed_sentences):
    counter = defaultdict(int)
    for sentence in parsed_sentences:
        for word in sentence:
            if word['pos'] != '記号':
                counter[word['base']] = counter.get(word['base'], 0) + 1
    ret = sorted([(word, freq) for word, freq in counter.items()],
                 key=lambda e: e[1], reverse=True)
    return ret


if __name__ == '__main__':
    filename = 'neko.txt.mecab'
    with open(filename, 'r') as f:
        data = f.read()

    parsed_sentences = parse(data)
    freqs = calc_word_frequency(parsed_sentences)
    # see examples
    pp.pprint(freqs[:20])
